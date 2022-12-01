#pylint:disable=C0114
import logging
import os
from pyrogram import Client
from pyrogram.errors import RPCError
from pyrogram.errors import BadRequest
# import asyncio
# from pyrogram.errors import FloodWait
# from pyrogram.handlers import MessageHandler
# os.environ['TZ'] = 'Asia/Kolkata'



logging.basicConfig(level=logging.INFO)



bot = Client(
    'bot',
    api_id= 27181638
, #get it from https://my.telegram.org/auth
    api_hash="c126672975f6f3f23f5276ef32b38f3a", #get it from https://my.telegram.org/auth
    bot_token="5857507263:AAHwkmqM2vd0PzaZy5o6_fvToM5hJq1_f0U", #get it from @Botfather
    plugins=dict(root="plugins"),
    parse_mode="html")


try:
    bot.run()
except Exception as e:
    print(e)
        