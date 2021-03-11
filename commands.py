from telegram.ext import Updater
from bs4 import BeautifulSoup
import requests


def start_command(update, context):
     message = "Merhaba ben Ulak, sana son dakika haberlerini getirmeye çalışacağım"

     return update.message.reply_text(message)


def wrong_command(update, context):
  message = "Hay aksi, kafam karıştı! Şimdilik yalnızca /start komutunu anlayabiliyorum"

  return update.message.reply_text(message)

def get_news(update, context):
     r = requests.get("https://www.haberler.com/son-dakika/")
     soup = BeautifulSoup(r.content, "lxml")

     news = soup.find_all('div', attrs={'class':"hblnBox"})
     my_new = str()

     for new in news[:3]:
          time = new.find("div", attrs = {'class':'hblnTime'}).text
          title = new.find('a', attrs={'class':"hblnTitle"}).get("title")
          link = new.find('a', attrs={'class':"hblnTitle"}).get("href")
  
  print("Time   : {}\nTitle  : {}\nLink   : {}".format(time, title, link))
  print("-"*20)