from telegram.ext import Application

# Read telegram api token
with open("bot_token.txt", "r") as f:
    TELEGRAM_API_TOKEN = f.read()

# This function trigger when someone start the bot with `/start` command
def start(update , context):
    application.updater.message.reply_text("Hey!\nWelcome to Pi-Fi guardian Telegram bot!")



application = Application.builder().token(TELEGRAM_API_TOKEN).build()
application.run_polling()

