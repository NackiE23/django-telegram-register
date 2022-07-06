from aiogram.dispatcher.filters.state import State, StatesGroup


class Register(StatesGroup):
    email = State()
    password = State()
    confirmation = State()
