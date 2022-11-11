from environ import Env
env = Env()
env.read_env()

import logging

from aiogram import Bot, Dispatcher, executor, types
from kurs import kurs
from waether import ob_havo
from help import help


import os
API_TOKEN = str(os.environ.get('BOT_TOKEN'))




#API_TOKEN = '5719510147:AAFgNkghqlqg1feVwD_3cNhgABQZcFeevpA'


# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    """
    This handler will be called when user sends `/start` or `/help` command
    """
    text = f"Assalomu alaykum {message.from_user.first_name} \nBotga hush kelibsiz.\n☁ Bu botdan ob-havo ma'lumotlarini va /kurs\n" \
           f"buyrig'i bilan kurs narxlarini bilib olishingiz mumkun"
    await message.answer(text)


@dp.message_handler(commands=['help'])
async def help_bot(message: types.Message):
    name = message.from_user.first_name
    data = help(name)

    await message.answer(data)


@dp.message_handler(commands=['kurs'])
async def usd_uzs_kurs(message: types.Message):
    data = kurs()

    await message.answer(data)



@dp.message_handler()
async def ob_havo_mal(message: types.Message):
    try:
        shahar = message.text
        data = ob_havo(shahar)
        await message.answer(data)
    except:
        await message.answer("Ma'lumot topilmadi")



if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)