from telegram.ext import Application, CommandHandler

# Read telegram api token
with open("bot_token.txt", "r") as f:
    TELEGRAM_API_TOKEN = f.read().strip()

# This function triggers when someone starts the bot with the `/start` command
async def start(update, context):
    await update.message.reply_text("Hey!\nWelcome to Pi-Fi guardian Telegram bot!")

# Create the application instance
application = Application.builder().token(TELEGRAM_API_TOKEN).build()

# Add a handler for the `/start` command
application.add_handler(CommandHandler("start", start))

# Run the bot
application.run_polling()
