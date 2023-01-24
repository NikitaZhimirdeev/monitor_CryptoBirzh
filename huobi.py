'''
https://open.huobigroup.com/?name=depth
'''

import requests

def huob():
    # ссылка api для получения курса btcusd
    url = 'https://api.huobi.pro/market/depth?symbol=btcusdt&depth=5&type=step0'

    headers = {"accept": "application/json"}
    # Отправляаем запрос
    response = requests.get(url, headers=headers)
    # Отправляем в main распаршеный json
    return response.json()['tick']['asks'][0][0]