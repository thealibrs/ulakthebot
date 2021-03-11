from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import commands as c
TOKEN = "your_token"

print("Bot çalışmaya başladı!")


def main():
    updater = Updater(TOKEN, use_context=True)
    dp = updater.dispatcher

    #my commands
    dp.add_handler(CommandHandler("start", c.start_command))
    dp.add_handler(CommandHandler("news", c.get_news))


    #while I write unknown word that the bot doesnt know
    dp.add_handler(MessageHandler(Filters.text, c.wrong_command))

    updater.start_polling()
    updater.idle()


if __name__ == "__main__":
    main()
