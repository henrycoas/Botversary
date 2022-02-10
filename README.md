# Botversary

Botversary is a Telegram Bot that, given a set of anniversaries, sends a message if there is a birthday today. 

Therefore, it needs to be executed everyday.

## Download or clone

1. Download the repository and open the main folder or simply execute the following commands:
```bash
git clone https://github.com/henrycoas/Botversary.git
cd Botversary
```

## Dependencies

2. This program is written in Python, and requires the following library:
```
sudo apt install pipenv
pipenv install --ignore-pipfile
```
You will also need to have Python installed. I used 3.8 version. Install it in order to be able to run the previous commands.

## Token setup

3. A TELEGRAM_TOKEN is needed for the bot to work. This corresponds to the bot API Token, so you will need to create a bot using BotFather and retrieve your bot's API Token.

I found this tutorial online which may be helpful if you don't know how to do it: 

[How to Create and Connect a Telegram Chatbot](https://sendpulse.com/knowledge-base/chatbot/create-telegram-chatbot)

4. Also, you will need your TELEGRAM_CHAT_ID. To get it:
 * In your browser, enter this Chat ID Link and replace YOUR_TOKEN with the Telegram API Token from your bot: 

https://api.telegram.org/YOUR_TOKEN/getUpdates?offset=0.

 * In your Telegram app, send your bot a message.
 * Again in your browser, update the page, identify your message and look for your id attribute: that's your TELEGRAM_CHAT_ID.

## Modify birthdays

Database example in *botversary/bdays_file.csv*:
```
first_name,last_name,day,month,year,note
Enric,Condal,19,3,2001,
Mr,Leap,29,3,,optional comment
```
 * Iff you fill the *year* attribute, the message will also contain the age of the birthday person.
 * The *note* attribute is also optional, no obligation to add it.
 * If there are no birthdays in the current day, the bot won't send any message.

5. To update the database with the changes done to the *bdays_file.csv*, remove the *botversaryDB.db* file (if it exists) and then run:
```bash
PYTHONPATH=$PYTHONPATH:$(pwd) pipenv run python botversary/runner.py --mode SEED --file botversary/bdays_file.csv
```

## Run

6. Execute the command:
```bash
TELEGRAM_TOKEN=<your_bot_telegram_token> TELEGRAM_CHAT_ID=<your_telegram_chat_id> PYTHONPATH=$PYTHONPATH:$(pwd) pipenv run python botversary/runner.py
```
You can also set both tokens in the *config.py* file, so you'll be able to shorten the previous command.

## Thanks

[Tutorial from Automagic I followed for the initial version](https://www.youtube.com/watch?v=KRn2xb1bxXM)

## Extensions
 * **[Done] Add how old is the birthday person**
   * Comments: May be easy for University or School friends but not for everyone, so it should be optional
 * **Run it once every morning**
   * Comments: In which server?
 * **Better messages**
   * Comments: Different colors, erase repetitive info related to today's date
