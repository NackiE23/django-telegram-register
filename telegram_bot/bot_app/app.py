from aiogram import Bot, Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage

API_KEY = "5340480719:AAHl6IdbpPN6HxCeu8Z-ucD_iXNkgKN7z0o"
REGISTRATION_API_URL = "http://nackie23.pythonanywhere.com/api/v1/create_user/"

bot = Bot(token=API_KEY)
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)
