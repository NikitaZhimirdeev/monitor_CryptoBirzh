'''
https://python-binance.readthedocs.io/en/latest/
https://binance-docs.github.io/apidocs/futures/en/#general-info

'''

import time
from binance import Client # pip install python-binance

# Формируем ключ входа
def auth_bin():
    apikey = 'O5Gm3NuFJtf2wrkJv8Cua4atsFTAxUk7B1xWSmBM1iX7bc9i9tg58ffJ45VQRJuQ'
    secret = 'KWKKLe1IPDJOGt2nxOQeX7KgRp3gAXlcjbFMwSZDMaGwdmzVukkXfC65HGhl9YJi'

    client = Client(apikey, secret)
    return client

# Получаем и отправляем курс
def bin(client):

    depth = client.get_order_book(symbol='BTCUSDT')
    return depth['bids'][0][0]
    # print(depth['bids'][0][0])
    # time.sleep(3)
    # print()

