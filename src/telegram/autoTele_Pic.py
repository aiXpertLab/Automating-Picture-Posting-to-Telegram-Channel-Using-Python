import os, random, shutil, telebot

from utils.utilities import RandomTitleGenerator

BOT_TOKEN = os.environ.get("TELE_TOKEN")
bot = telebot.TeleBot(BOT_TOKEN)

channel_name = "-1002126729483"   #asiagirl
# channel_name = "-4061783014"        #ycc

caption = RandomTitleGenerator("./src/telegram/resources/captions.txt")

source="E:/gDrive/38.Pic/Tele"
dest  ="E:/gDrive/38.Pic/Tele/web"

random_file=random.choice(os.listdir(source))
source_file="%s/%s"%(source,random_file)
shutil.move(source_file,dest)
dest_file="%s/%s"%(dest,random_file)
photo = open(dest_file, 'rb')

bot.send_photo(channel_name, photo, caption=caption.get_random_line())
# bot.send_message(chat_id=channel_name, text="day day asian girl 3")
# bot.infinity_polling()     