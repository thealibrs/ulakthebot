from telegram.ext import Updater


def start_command(update, context):
     message = "Merhaba ben Ulak, sana son dakika haberlerini getirmeye çalışacağım"

     return update.message.reply_text(message)


def wrong_command(update, context):
  message = "Hay aksi, kafam karıştı! Şimdilik yalnızca /start komutunu anlayabiliyorum"

  return update.message.reply_text(message)
