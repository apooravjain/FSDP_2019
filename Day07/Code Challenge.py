
import json
import requests

Host = "https://enl32051nvg7s.x.pipedream.net"

data = {"firstname":"Apoorav","language":"English"}

headers = {"Content-Type":"application/json","Content-Length":len(data),"data":json.dumps(data)}

def post_method():
    response = requests.post(Host,data,headers)
    return response

print ( post_method().text )


