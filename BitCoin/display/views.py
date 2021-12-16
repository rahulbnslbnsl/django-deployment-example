from django.shortcuts import render
import requests

# Create your views here.
def index(request):
    # return render(request,'index.html',context={'text': "Hello World"})
    # url = 'ws://localhost:8000/wss://fxws.gateio.ws/v4/ws/btc/'
    # coins = requests.get(url).json()
    data = {'time':'Time1','open':45346,'close':1234,'Highest':56,'Lowest':20,'volume':20}
    return render(request,'index.html',context={'data': data })
