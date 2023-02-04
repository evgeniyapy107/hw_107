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


class meinfo(StatesGroup):
    Q1 = State()
    Q2 = State()


@dp.message_handler(Command("me"), state=None)
async def enter_meinfo(message: types.Message):
    if message.chat.id == config.admin:
        await message.answer("начинаем настройку. \n" "N1 введите линк на ваш профиль")
        await meinfo.Q1.set()


@dp.message_handler(state=meinfo.Q1)
async def answer_q1(message: types.Message, state: FSMContext):
    answer = message.text
    await state.update_data(answer1=answer)
    await message.answer("Линк сохранен. \n"
                         "№2 Введите текст")
    await meinfo.Q2.set()


@dp.message_handler(state=meinfo.Q2)
async def answer_q1(message: types.Message, state: FSMContext):
    answer = message.text
    await state.update_data(answer2=answer)
    await message.answer("Текст сохранен")
    data = await state.get_data()
    answer1 = data.get("answer1")
    answer2 = data.get("answer2")

    joinedFile = open("link.txt", "w", encoding="utf-8")
    joinedFile.write(str(answer1))
    joinedFile = open("text.txt", "w", encoding="utf-8")
    joinedFile.write(str(answer2))
    await message.answer(f'Ваша ссылка на профиль: {answer1}\n Ваш текст: \n{answer2}')
    await state.finish()


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


@dp.message_handler(content_types=['text'])
async def get_message(message):
    if message.text == "Информация":
        await bot.send_message(message.chat.id, text="Информация\nБот создан специально для обучения",
                               parse_mode='Markdown')
    elif message.text == "Статистика":
        await bot.send_message(message.chat.id, text="Хочешь посмотреть статистику бота?", reply_markup=keyboard.stats,
                               parse_mode='Markdown')
    elif message.text == "Разработчик":
        link1 = open('link.txt', encoding="utf-8")
        link = link1.read()

        text1 = open('text.txt', encoding="utf-8")
        text = text1.read()
        await bot.send_message(message.chat.id, text=f"Создатель: {link}\n{text}", parse_mode='HTML')
    elif message.text == "Покажи пользователя":
        await bot.send_message(message.chat.id, text=f"пользователь - {message.from_user.first_name}",
                               reply_markup=keyboard.userkeyboard,
                               parse_mode='Markdown')
    elif message.text == "Добавить фото":
        await bot.send_message(message.chat.id, text="Добавьте фото:",
                               parse_mode='Markdown')


"""
@dp.message_handler(content_types=['photo'])
async def photo_id(message):
    try:

"""


@dp.message_handler(commands="info")
async def cmd_test1(message: types.Message):
    await message.reply("Бот создан для обучения")


@dp.callback_query_handler(text_contains='join')
async def join(call: types.CallbackQuery):
    if call.message.chat.id == config.admin:
        d = sum(1 for line in open('user.txt'))
        await bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                    text=f'Вот статистика бота: *{d}* человек', parse_mode='Markdown')
    else:
        await bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                    text=f'У тебя нет админки\n Куда ты полез', parse_mode='Markdown')


@dp.callback_query_handler(text_contains='cancle')
async def cancle(call: types.CallbackQuery):
    await bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                text=f'ты вернулся в главное меню. Жми опять кнопки', parse_mode='Markdown')


@dp.callback_query_handler(text_contains='view')
async def view(call: types.CallbackQuery):
    await bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                text=f'твой id - {call.message.chat.id}', parse_mode='Markdown')


@dp.callback_query_handler(text_contains='exit')
async def exit(call: types.CallbackQuery):
    await bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                text=f'вы отменили выбор', parse_mode='Markdown')


@dp.message_handler(commands=['rassilka'])
async def rassilka(message):
    if message.chat.id == config.admin:
        await bot.send_message(message.chat.id, f"*Рассылка началась \nБот оповестит, когда закончит рассылку*",
                               parse_mode='Markdown')
        receive_users, block_users = 0, 0
        joinedFile = open("user.txt", "r")
        joinedUsers = set()
        for line in joinedFile:
            joinedUsers.add(line.strip())
        joinedFile.close()
        for user in joinedUsers:
            try:
                await bot.send_photo(user, open('photo.png', 'rb'), message.text[message.text.find(' '):])
                receive_users += 1
            except:
                block_users += 1
            await asyncio.sleep(0.4)
        await bot.send_message(message.chat.id, f"*Рассылка была завершена *\n"
                                                f"получили сооющение: *{receive_users}*\n"
                                                f"заблокировали бота: *{block_users}*", parse_mode='Markdown')


if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
