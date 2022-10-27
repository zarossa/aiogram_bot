import string

from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
import os, json

bot = Bot(token=os.getenv('TOKEN'))
dp = Dispatcher(bot)


async def on_startup(_):
    print('Bot is online')


'''Клиентская часть'''


@dp.message_handler(commands=['start', 'help'])
async def command_start(message: types.Message):
    try:
        await bot.send_message(message.from_user.id, 'Приятного аппетита')
        # await message.delete()
    except:
        await message.reply('Общение с ботом через ЛС, напишите ему:\nhttps://t.me/zarossa_test1_bot')


@dp.message_handler(commands=['Режим_работы'])
async def pizza_open_command(message: types.Message):
    try:
        await bot.send_message(message.from_user.id, 'Пн-ВС круглосуточно')
        # await message.delete()
    except:
        await message.reply('Общение с ботом через ЛС, напишите ему:\nhttps://t.me/zarossa_test1_bot')


@dp.message_handler(commands=['Расположение'])
async def pizza_place_command(message: types.Message):
    try:
        await bot.send_message(message.from_user.id, 'ул. Юрная 11')
        # await message.delete()
    except:
        await message.reply('Общение с ботом через ЛС, напишите ему:\nhttps://t.me/zarossa_test1_bot')


'''Админская часть'''

'''Общая часть'''


@dp.message_handler()
async def echo_send(message: types.Message):
    if {i.lower().translate(str.maketrans('', '', string.punctuation)) for i in message.text.split()}.intersection(set(json.load(open('cenz.json')))) != set():
        await message.reply('Маты запрещены')
        await message.delete()


executor.start_polling(dp, skip_updates=True, on_startup=on_startup)
