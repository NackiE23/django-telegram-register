from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


confirmation_keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Yes"),
            KeyboardButton(text="No"),
        ]
    ],
    resize_keyboard=True
)
