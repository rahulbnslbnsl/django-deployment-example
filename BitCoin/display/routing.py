from django.urls import path
from .consumer import WSConsumer

ws_urlpatterns = [
    # ‘wss://fxws.gateio.ws/v4/ws/btc’
    # path('wss://fxws.gateio.ws/v4/ws/btc',WSConsumer.as_asgi())
    path('ws/some_url/',WSConsumer.as_asgi())
]
# import requests
#
# host = "https://api.gateio.ws"
# prefix = "/api/v4"
# headers = {'Accept': 'application/json', 'Content-Type': 'application/json'}
#
# url = '/futures/usdt/candlesticks'
# query_param = 'contract=BTC_USDT'
# r = requests.request('GET', host + prefix + url + "?" + query_param, headers=headers)
# print(r.json())
# key api = 18afb18f1914cb379812b714c50f5ab7
# secret key = 6999d0588d4be878325ca8abaa5e64daebea8bf12b6d06fd7205fc520dd249bc
# api and secret keys = {"apiKey":"18afb18f1914cb379812b714c50f5ab7","secretKey":"6999d0588d4be878325ca8abaa5e64daebea8bf12b6d06fd7205fc520dd249bc"}
