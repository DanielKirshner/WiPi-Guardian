from telegram.ext import CommandHandler

class BotCommandHandlers:
    def __init__(self, bot_runner):
        self.bot_runner = bot_runner

    async def hello(self, update, context):
        await update.message.reply_text("Hey!\nWelcome to Pi-Fi guardian Telegram bot!")

    async def is_network_up(self, update, context):
        await update.message.reply_text("Network is up!")
