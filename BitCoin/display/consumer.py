import json
from random import randint
from time import sleep
import time
from websocket import create_connection
from channels.generic.websocket import WebsocketConsumer
from asgiref.sync import async_to_sync

# ws = create_connection("wss://fxws.gateio.ws/v4/ws/btc/")
# ws.send(json.dumps({
#     "time": int(time.time()),
#     "channel": "futures.candlesticks",
#     "event": "subscribe",  # "unsubscribe" for unsubscription
#     "payload": ["10s", "BTC_USDT"]
# }))
# print(ws.recv())

class WSConsumer(WebsocketConsumer):
    def connect(self):
        self.room_name = "test_consumer"
        self.room_group_name = "test_consumer_group"
        async_to_sync(self.channel_layer.group_add(self.room_name,self.room_group_name))

        self.accept()
        # self.send()

        self.send(text_data = json.dumps('{"status" : "socket connect t t"}'))

        # for i in range(1000):
        #     self.send(json.dumps({'message': randint(1,100)}))
        #     sleep(1)

    def receive(self,text_data):
        # print(text_data)
        # textdata_json = json.loads(text_data)
        # textdata_json['message'] +=' echo'
        # self.send(json.dumps(text_data))
        pass
