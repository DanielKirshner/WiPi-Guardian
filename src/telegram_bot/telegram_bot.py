from telegram.ext import Application, CommandHandler
import logging

class TelegramBotRunner:
    def __init__(self, token):
        self.application = Application.builder().token(token).build()
        self._register_all_handlers()
    
    def __enter__(self):
        logging.info("Telegram bot is up.")
        self.application.run_polling()
        return self

    def _register_all_handlers(self):
        self.application.add_handler(CommandHandler("start", self.start))

    async def start(self, update, context):
        await update.message.reply_text("Hey!\nWelcome to Pi-Fi guardian Telegram bot!")

    def __exit__(self, exc_type, exc_value, traceback):
        logging.info("Telegram bot is shutting down.")
