from aiogram.utils import executor
from bot_app import dp, storage


async def shutdown(dp):
    await storage.close()


executor.start_polling(dp, on_shutdown=shutdown)
