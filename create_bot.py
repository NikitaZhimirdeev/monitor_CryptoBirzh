# Создаем подключение к боту
from aiogram import Bot
import os
from aiogram.dispatcher import Dispatcher


bot = Bot(token='5754179224:AAHucKSf26Eoc0vX3Oepauvzvv5kRefIzfA')
# bot = Bot(token=os.getenv('TOKEN'))
dp = Dispatcher(bot)
