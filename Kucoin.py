"""
Kucoin

Лимит подключений: 30 в минуту
Лимит сообщений, отправляемых на сервер: 100 за 10 секунд
"""

import hmac
import base64
import hashlib
import time
import requests

# Формируем ключ входа
def auth_kucoin():
    # Задаем ключи входа
    api_key = "api_key"
    api_secret = "api_secret"
    api_passphrase = "api_passphrase"

    # api ссылка для get запроса получения курса
    url = 'https://api-futures.kucoin.com/api/v1/mark-price/XBTUSDTM/current'

    # получаем время для формирования ссылок
    now = int(time.time() * 1000)
    # Формируем ссылку подписи
    str_to_sign = str(now) + 'GET' + '/api/v1/position?symbol=XBTUSDTM/current'

    # формируем подпись и переводим ее в base64
    signature = base64.b64encode(
        hmac.new(api_secret.encode('utf-8'), str_to_sign.encode('utf-8'), hashlib.sha256).digest())

    # формируем кодовую фразу и переводим ее в base64
    passphrase = base64.b64encode(
        hmac.new(api_secret.encode('utf-8'), api_passphrase.encode('utf-8'), hashlib.sha256).digest())

    # Составлем заголовки запроса
    headers = {
        "KC-API-SIGN": signature,
        "KC-API-TIMESTAMP": str(now),
        "KC-API-KEY": api_key,
        "KC-API-PASSPHRASE": passphrase,
        "KC-API-KEY-VERSION": "2"
    }
    return url, headers

#
def kuc(url, headers):
    # Отправляем запрос для получения курса
    response = requests.request('get', url, headers=headers)
    # Отправляем в main распаршеный json
    return response.json()['data']['indexPrice']


