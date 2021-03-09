from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
TOKEN = "1685639520:AAHf0jD739qNURYHedUZSlYx-3GCrX91ts8"

print("Bot çalışmaya başladı!")


def main():
    updater = Updater(TOKEN, use_context=True)
    dp = updater.dispatcher

    updater.start_polling(1.5)
    updater.idle()


if __name__ == "__main__":
    main()
