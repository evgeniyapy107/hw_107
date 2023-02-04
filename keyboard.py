from aiogram import Bot, types
from aiogram.types import ReplyKeyboardRemove, ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, \
    InlineKeyboardButton

start = types.ReplyKeyboardMarkup(resize_keyboard=True)
info = types.KeyboardButton("Информация")
stats = types.KeyboardButton("Статитстика")
razrab = types.KeyboardButton("Разработчик")
userkey = types.KeyboardButton("Покажи пользователя")
add_photo = types.KeyboardButton("Добавить фото")
show_photo = types.KeyboardButton("показать фото из галереи")
start.add(stats, info)
start.add(razrab, userkey)
start.add(add_photo, show_photo)
stats = InlineKeyboardMarkup()
stats.add(InlineKeyboardMarkup(f'Да', callback_data='join'))
stats.add(InlineKeyboardMarkup(f'Нет', callback_data='cancle'))
userkeyboard = InlineKeyboardMarkup()
userkeyboard.add(InlineKeyboardMarkup('хочу увидеть id', callback_data='view'))
userkeyboard.add(InlineKeyboardMarkup('вернуться обратно', callback_data='exit'))
