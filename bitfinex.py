"""
https://docs.bitfinex.com/docs/open-source-libraries

90 запросов в минуту;  блокируется на 60 секунд
"""

import time
import requests

# Получаем и отправляем курс
def bitf():
    # ссылка api для получения курса btcusd
    url = "https://api-pub.bitfinex.com/v2/ticker/tBTCUSD"

    headers = {"accept": "application/json"}

    # Отправляаем запрос
    response = requests.get(url, headers=headers)
    # Отправляем в main распаршеный json
    return response.json()[-4]

