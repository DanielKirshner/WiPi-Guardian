from telegram.ext import Application, CommandHandler
from telegram_bot.command_handlers import BotCommandHandlers
import logging

class TelegramBotRunner:
    def __init__(self, token):
        self.application = Application.builder().token(token).build()
        self.command_handlers = BotCommandHandlers(self)
        self.__register_all_handlers()
    
    def __enter__(self):
        logging.info("Telegram bot is up.")
        self.application.run_polling()
        return self

    def __register_all_handlers(self):
        for command_name in dir(self.command_handlers):
            if not command_name.startswith('_'):  # Skip private methods
                handler_function = getattr(self.command_handlers, command_name)
                if callable(handler_function):
                    self.application.add_handler(CommandHandler(command_name, handler_function))


    def __exit__(self, exc_type, exc_value, traceback):
        logging.info("Telegram bot is shutting down.")
