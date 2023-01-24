import json
from aiogram import executor, types
from create_bot import dp, bot
import asyncio

from binance_api import bin, auth_bin
from bitstamp import bits
from huobi import huob
from bitfinex import bitf
import os
from Kucoin import kuc, auth_kucoin

# Команда запуска и добавления новых пользователей бота
@dp.message_handler(commands=['start'])
async def START(message: types.Message):
    # Сбор всех id пользователей, которые активировали бота
    with open('users.txt', 'r') as f:
        users = ''.join(f.readlines()).strip().split('\n')

    # Проверяем на наличие в списке акнтивации
    if not (str(message.from_user.id) in users):
        with open('users.txt', 'a') as f:
            f.write(f'{message.from_user.id}\n')

        await message.answer('append user')
    await main()

# Оснаваня функция проверки курса на разных площадках
async def main():
    # Создаем вход для полщадок, где это необходимо
    client_binance = auth_bin()
    url_kucoin, headers_kucoin = auth_kucoin()

    # Получаем настройки запуска
    with open('settings.json', 'r', encoding='utf-8') as file:
        settings = json.load(file)
    dif = float(settings['dif'])        # процент разницы
    sleep = float(settings['sleep'])    # интервал между запросами

    # Получаем список активных пользователей
    with open('users.txt', 'r') as f:
        users = ''.join(f.readlines()).strip().split('\n')

    # Запускаем мониторинг площядок
    while True:
        try:
            # Задаем словарь хранения <цена>:<биржа>
            curs_name = {}

            # Получаем данные с каждой биржи
            btc_usd_binance = float(bin(client_binance))
            curs_name[btc_usd_binance] = 'Binance'

            btc_usd_bitstamp = float(bits())
            curs_name[btc_usd_bitstamp] = 'Bitstamp'

            btc_usd_huobi = float(huob())
            curs_name[btc_usd_huobi] = 'Huobi'

            btc_usd_bitfinex = float(bitf())
            curs_name[btc_usd_bitfinex] = 'Bitfinex'

            btc_usd_kucoin = float(kuc(url_kucoin, headers_kucoin))
            curs_name[btc_usd_kucoin] = 'Kucoin'

            # Получаем максимум и минимум
            max_curs = max(curs_name)
            min_curs = min(curs_name)
            # print()

            # Сравниваем с минимальной разницой в процентах
            if max_curs/min_curs*100 - 100 >= dif:
                # Формируем сообщение
                MES = f"% - {max_curs/min_curs*100 - 100}\n" \
                      f"MAX - {curs_name[max_curs]} - {max_curs}\n" \
                      f"MIN - {curs_name[min_curs]} - {min_curs}"
                # print(max_curs/min_curs*100 - 100)
                # Отправка сообщения
                for user in users:
                    await bot.send_message(chat_id=user, text=MES)

            # Останавливаем алгоритм на заданное кол-во секунд
            await bot.send_message(chat_id=657572123, text=f'{max_curs/min_curs*100 - 100}')
            await asyncio.sleep(sleep)
        except:
            break
    await main()


# Запуск программы
if __name__ == '__main__':
    # Запуск бота
    executor.start_polling(dp, skip_updates=True)

