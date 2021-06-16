import os
import glob
cookie_del = glob.glob("config/*cookie.json")
os.remove(cookie_del[0])
from instabot import Bot
bot = Bot()
bot.login(username="insta_id", password="password")
bot.upload_photo("image or video", caption="optional")
