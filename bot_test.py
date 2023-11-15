from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

def start(update, context):
    update.message.reply_text('Привет! Я ваш эхо-бот Раз дав три четыре 6.')

def echo(update, context):
    received_text = update.message.text
    update.message.reply_text(received_text)

def main():
    TOKEN = 'ВАШ_ТОКЕН_ЗДЕСЬ'

    updater = Updater(TOKEN, use_context=True)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(MessageHandler(Filters.text & ~Filters.command, echo))

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
