import os
from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext

TOKEN = os.getenv("8132471722:AAHM4HMuQUtd4Dqpppu7793FBZVNZ1_86NI")

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
