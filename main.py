import logging
from aiogram import Bot, Dispatcher, executor, types
from aiogram.utils import executor
import asyncio
from aiogram.dispatcher import Dispatcher
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Command
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import StatesGroup, State
import config
import keyboard
import logging

storage = MemoryStorage()
bot = Bot(token=config.botkey, parse_mode=types.ParseMode.HTML)
dp = Dispatcher(bot, storage=storage)
logging.basicConfig(format=u'(filename)s [LINE:%(lineno)d] #%(levelname)-8s [%(asctime)s] %(message)s',
                    level=logging.INFO)


@dp.message_handler(Command("start"), state=None)
async def welcome(message):
    joinedFile = open("user.txt", "r")
    joinedUsers = set()
    for line in joinedFile:
        joinedUsers.add(line.strip())

    if not str(message.chat.id) in joinedUsers:
        joinedFile = open("user.txt", "a")
        joinedFile.write(str(message.chat.id) + "\n")
        joinedUsers.add(message.chat.id)

    await bot.send_message(message.chat.id, f"ПРИВЕТ, *{message.from_user.first_name}, *БОТ РАБОТАЕТ",
                           reply_markup=keyboard.start, parse_mode='Markdown')


@dp.message_handler(commands="info")
async def cmd_test1(message: types.Message):
    await message.reply("Бот создан для обучения")


if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
