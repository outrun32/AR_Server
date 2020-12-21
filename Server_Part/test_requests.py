import json
import requests
import socket
hostname = socket.gethostname()
local_ip = socket.gethostbyname(hostname)
dictToSend = {"local":str(local_ip)}
res = requests.post('http://192.168.43.84:5000/data', json=dictToSend)
print(res.text)