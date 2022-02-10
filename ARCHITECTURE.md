# Requirements

 * Store data about friends/family/...'s birthdays.
 * Read data about birthdays.
 * Understand if today there is one or more bdays.
 * Handle leap year birthdays.
 * Add / Remove / Update bday data.
 * Integrate with some notification / messaging API.
 * Can send messages via that API.

# Data Model

 * DB Models
   * Birthday
     * first_name
     * last_name
     * day
     * month
     * year
     * note
     * dt_created
     * dt_updated
 * Messaging / API Handler
   * Create client / connect to API
   * Send message
 * Config
   * Constants
 * Runner
   * Db connection objects
   * Main function

# Happy Path

1. Read config file, instantiate logger.
2. Read database to get birthdays.
3. See if today is a birthday.
4. For all birthdays today, notify us.
5. Exit.
