from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext

# Вставь сюда токен, который получишь от @BotFather
TELEGRAM_BOT_TOKEN = "7423756548:AAErpLCCmAcRRe6gt_CCYds2q9ekVnqEOww"

def start(update: Update, context: CallbackContext):
    update.message.reply_text("Привет! Я - Hello Bot.\n"
                              "Используй /help для списка команд.")

def help_command(update: Update, context: CallbackContext):
    update.message.reply_text("Доступные команды:\n"
                              "/start - начало работы\n"
                              "/help - помощь")

def main():
    updater = Updater(TELEGRAM_BOT_TOKEN)

    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(CommandHandler("help", help_command))

    updater.start_polling()
    updater.idle()

if __name__ == "__main__":
    main()
