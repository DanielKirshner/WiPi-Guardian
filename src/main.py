from telegram_bot.telegram_bot import TelegramBotRunner
from common import logger
import logging
import os

def main():
    logger.init()
    
    try:
        BOT_TOKEN_FILE_PATH = os.path.join("config", "bot_token.txt")
        
        with open(BOT_TOKEN_FILE_PATH, "r") as f:
            TELEGRAM_API_TOKEN = f.read().strip()
    except FileNotFoundError:
        logging.error(f"{BOT_TOKEN_FILE_PATH} file not found.")
        return
    
    with TelegramBotRunner(TELEGRAM_API_TOKEN) as bot:
        pass


if __name__ == "__main__":
    main()
