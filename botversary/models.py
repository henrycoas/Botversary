import calendar
import datetime
import logging

import dateutil.parser

import pytz
from sqlalchemy import select
from sqlalchemy import (Column, Integer, String, DateTime, Boolean)
from sqlalchemy.schema import UniqueConstraint

from botversary import config


# Birthday model.
class Birthday(config.Base):

    __tablename__ = "birthdays"

    id = Column(Integer, primary_key=True)
    first_name = Column(String, nullable=False)
    last_name = Column(String, nullable=False)
    day = Column(Integer, nullable=False)
    month = Column(Integer, nullable=False)
    year = Column(Integer)
    note = Column(String)
    dt_created = Column(DateTime, default=datetime.datetime.utcnow)
    dt_updated = Column(DateTime, default=datetime.datetime.utcnow)

    __table_args__ = (
        UniqueConstraint("first_name", "last_name", name="_first_last_uc"),
    )

    # Creates a Birthday object.
    @classmethod
    def create_birthday(cls, record):
        """
        Args:
            record: Dict containing birthday data. Fields (keys) should match:
                first_name: str, The person's first name.
                last_name: str, The person's last name.
                day: int, The numeric representation of the day (1-31).
                month: int, The numeric representation of the month (1-12).
                year: int OPTIONAL, The numeric representation of the year (*-current_year)
                note: str OPTIONAL, A note associated with this person
                    (e.g. X's husband).
                dt_updated: str OPTIONAL, Datetime string for the update date
                    of this record in UTC time.
        Returns:
            An instantiated Birthday instance.
        """
        if record["day"] not in range(1, 32):
            raise ValueError("Day must be between 1 and 31 inclusive.")

        if record["month"] not in range(1, 13):
            raise ValueError("Month must be between 1 and 12 inclusive.")

        if record["year"] > datetime.datetime.now().year:
            raise ValueError("Year must be smaller or equal than current year.")


        data_dict = {
            "first_name": record["first_name"].lower(),
            "last_name": record["last_name"].lower(),
            "day": record["day"],
            "month": record["month"],
            "year": record.get("year"),
            "note": record.get("note")
        }

        dt_updated = record.get("dt_updated")
        if dt_updated:
            data_dict["dt_updated"] = dateutil.parser.parse(
                dt_updated).replace(tzinfo=pytz.utc)

        return cls(**data_dict)

    # Queries the database to get all records with a birthday in month.
    @classmethod
    def get_birthdays_for_month(cls, session, month):
        """
        Args:
            session: An initialized SQLAlchemy session object.
            month: int, The month to search (most likely the current month).
        Returns:
            All database records with birthdays in month.
        """
        return session.execute(
            select(cls).where(cls.month == month)
        ).scalars().all()

    def __str__(self):
        """Format a birthday string as mrkdwn so we can easily send messages."""
        fmt = (
            f"<b>{self.first_name.capitalize()} "
            f"{self.last_name.capitalize()}</b> ("
            f"{calendar.month_name[self.month]} {self.day})"
        )

        if self.year is not None:
            age = datetime.date.today().year - self.year
            fmt += f":\n{age} y/o"

        if self.note:
            fmt += f",\n<i>{self.note.capitalize()}</i>"

        return fmt