# Developed by nomiss7

from aiogram import Bot
from aiogram.dispatcher import Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage

from config import TOKEN_API
from databases.database import MyDb

db = MyDb()

storage = MemoryStorage()
bot = Bot(TOKEN_API)
dp = Dispatcher(bot, storage=storage)

chat_id = -1001685066059

# mute time
time_example = 21600
# time_example = 60
