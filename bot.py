from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext
import os

# Получаем токен из переменной среды
TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")

def start(update: Update, context: CallbackContext):
    update.message.reply_text("Привет! Я - Hello Bot.\n"
                              "Используй /help для списка команд.")

def help_command(update: Update, context: CallbackContext):
    update.message.reply_text("Доступные команды:\n"
                              "/start - начало работы\n"
                              "/help - помощь")

def main():
    if not TELEGRAM_BOT_TOKEN:
        raise ValueError("Не установлен токен бота. Установите переменную среды TELEGRAM_BOT_TOKEN.")
    
    updater = Updater(TELEGRAM_BOT_TOKEN)
    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(CommandHandler("help", help_command))

    updater.start_polling()
    updater.idle()

if __name__ == "__main__":
    main()
