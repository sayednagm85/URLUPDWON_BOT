import os
from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext

TOKEN = os.getenv("URLUPDWON_BOT")

def start(update: Update, context: CallbackContext) -> None:
    update.message.reply_text("مرحبًا! هذا بوت تحميل الفيديوهات من الروابط.")

def main():
    updater = Updater(TOKEN)
    dp = updater.dispatcher
    dp.add_handler(CommandHandler("start", start))
    updater.start_polling()
    updater.idle()

if __name__ == "__main__":
    main()
