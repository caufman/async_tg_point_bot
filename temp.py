import logging

from aiogram import Bot, Dispatcher, executor, types

API_TOKEN = "856212558:AAHjTTJvmNATH8_oH-7kwUyOIZO9nDp3TEg"

logging.basicConfig(level=logging.INFO)

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start','help'])
async def send_welcome(message: types.Message):
    await message.reply("пробный бот by cauf приветствует тебя!")

@dp.message_handler()
async def echo(message: types.Message):
    await bot.send_message(message.chat.id, message.text)

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)

