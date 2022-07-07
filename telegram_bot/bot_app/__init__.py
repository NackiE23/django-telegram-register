import logging
from .app import dp, storage, bot, API_KEY
from . import handlers

logging.basicConfig(level=logging.INFO)
