from aiogram.utils import executor
from bot_app import dp, storage, bot, API_KEY

# webhook settings
WEBHOOK_HOST = 'https://django-telegram-register-bot.herokuapp.com/'
WEBHOOK_PATH = f'/{API_KEY}'
WEBHOOK_URL = f"{WEBHOOK_HOST}{WEBHOOK_PATH}"

# webserver settings
WEBAPP_HOST = 'localhost'
WEBAPP_PORT = 8000


async def startup(dp):
    await bot.set_webhook(WEBHOOK_URL)


async def shutdown(dp):
    await bot.delete_webhook()
    await storage.close()


if __name__ == "__main__":
    # executor.start_polling(dp, on_shutdown=shutdown)
    executor.start_webhook(dispatcher=dp,
                           webhook_path=WEBHOOK_PATH,
                           on_startup=startup,
                           on_shutdown=shutdown,
                           skip_updates=True,
                           host=WEBAPP_HOST,
                           port=WEBAPP_PORT)
