import os

from sqlalchemy.ext.declarative import declarative_base


# Sets the log file to the path provided or defaults to the tmp folder.
LOGFILE = os.environ.get("LOGFILE", "/tmp/botversarylog")

# Database configuration
DATABASE = os.environ.get("DATABASE", "sqlite:///botversaryDB.db")
Base = declarative_base()

# Telegram constants
    # Can be set here or in the environment you are working on
    # Format: TELEGRAM_TOKEN = '0123456789:ABC-DEF1234ghIkl-zyx57W2v1u123ew11'
    # Format: TELEGRAM_CHAT_ID = '0123456789'
TELEGRAM_TOKEN = os.environ.get("TELEGRAM_TOKEN")
TELEGRAM_CHAT_ID = os.environ.get("TELEGRAM_CHAT_ID")
