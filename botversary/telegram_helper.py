import telegram
from telegram import Bot

from botversary import config


class TelegramFacade(object):

    def __init__(self, token=config.TELEGRAM_TOKEN,
                 cid=config.TELEGRAM_CHAT_ID):
        self.token = token
        self.chat_id = cid
        self.client = Bot(self.token)
        
    # Sends a markdown message to our telegram user.
    def send_message(self, message):
        # Args:
        #     message: String, markdown representing a message to send.
        # Returns:
        #     Telegram response object.

        return self.client.send_message(
            self.chat_id,
            message,
            parse_mode = telegram.ParseMode.HTML
        )