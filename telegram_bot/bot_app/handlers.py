import requests

from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text
from aiogram.types import Message, ReplyKeyboardRemove
from django.core.exceptions import ValidationError
from django.core.validators import validate_email

from .app import dp, REGISTRATION_API_URL
from .register import Register
from .keyboards import confirmation_keyboard


@dp.message_handler(commands=['start', 'help'])
async def welcome(message: Message):
    await message.reply("You can register to site by clicked on /register")


@dp.message_handler(commands=['register'], commands_prefix="!/", state=None)
async def register(message: Message):
    await message.answer("Enter your email")
    await Register.email.set()


@dp.message_handler(state=Register.email)
async def enter_email(message: Message, state: FSMContext):
    email = message.text
    try:
        validate_email(email)
    except ValidationError:
        await message.answer("It's not a valid email!")
        await state.finish()
        await register(message=message)
    else:
        await state.update_data({'email': email})

        await message.answer("Enter your password")
        await Register.next()


@dp.message_handler(state=Register.password)
async def enter_password(message: Message, state: FSMContext):
    data = await state.get_data()
    password = message.text
    await state.update_data({'password': password})

    await message.answer(f"Email: {data.get('email')}; Password: {password}. All right?", reply_markup=confirmation_keyboard)
    await Register.next()


@dp.message_handler(Text(equals=['Yes', 'No']), state=Register.confirmation)
async def confirmation(message: Message, state: FSMContext):
    answer = message.text

    if answer == "Yes":
        data = await state.get_data()
        data.update({
            'user_id': str(message.from_user.id),
            'username': message.from_user.username,
            'name': message.from_user.first_name,
        })
        try:
            requests.post(REGISTRATION_API_URL, json=data)
        except requests.exceptions.ConnectionError:
            await message.answer("Server is dead", reply_markup=ReplyKeyboardRemove())
            await state.finish()
        else:
            await message.answer(f"Congratulations! You're successfuly registered! \n"
                                 f"You can login using this link http://nackie23.pythonanywhere.com/login/",
                                 reply_markup=ReplyKeyboardRemove())
            await state.finish()
    else:
        await message.answer("Okay! Have a nice day.", reply_markup=ReplyKeyboardRemove())
        await state.finish()
