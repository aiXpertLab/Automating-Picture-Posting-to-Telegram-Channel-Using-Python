import os, random, shutil, telebot
from dotenv import load_dotenv

from utils.utilities import RandomTitleGenerator

load_dotenv()
BOT_TOKEN = os.environ.get("TELE_TOKEN")
bot = telebot.TeleBot(BOT_TOKEN)

channel_name1 = "-1002126729483"   #asiagirl
# channel_name2 = "-4061783014"        #ycc

caption = RandomTitleGenerator("a:/autoTele/src/telegram/resources/captions.txt")

source="E:/gDrive/38.Pic/Tele"
dest  ="E:/gDrive/38.Pic/Tele/web"

random_file=random.choice(os.listdir(source))
source_file="%s/%s"%(source,random_file)
shutil.move(source_file,dest)
dest_file="%s/%s"%(dest,random_file)
photo = open(dest_file, 'rb')

bot.send_photo(channel_name1, photo, caption=caption.get_random_line())
# bot.send_message(chat_id=channel_name, text="day day asian girl 3")
# bot.infinity_polling()     