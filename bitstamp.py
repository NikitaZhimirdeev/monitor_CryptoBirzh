'''
https://www.bitstamp.net/api/
8000 запросов в течение 10 минут
'''

import requests
import time

# Получаем и отправляем курс
def bits():

    # ссылка api для получения курса btcusd
    url = 'https://www.bitstamp.net/api/v2/transactions/btcusd/'

    # Отправляаем запрос через прокси
    response = requests.get(url, proxies={'https': 'http://LQCbWv:ZxErKc@193.3.177.94:8000'})

    # Отправляем в main распаршеный json
    return response.json()[0]['price']
    # print(response.json()[0]['price'])

