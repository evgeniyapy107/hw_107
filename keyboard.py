from aiogram import Bot, types
from aiogram.types import ReplyKeyboardRemove, ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, \
    InlineKeyboardButton

start = types.ReplyKeyboardMarkup(resize_keyboard=True)
info = types.KeyboardButton("Информация")
stats = types.KeyboardButton("Статитстика")
start.add(stats, info)
