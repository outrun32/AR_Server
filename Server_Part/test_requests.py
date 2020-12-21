import json
import requests
import socket
hostname = socket.gethostname()
local_ip = socket.gethostbyname(hostname)
dictToSend = {"ip":str(local_ip)}
def add():
    res = requests.post('http://172.17.7.225:5000/data_append', json=dictToSend)
    print(res.text)
def delete():
    res = requests.delete('http://172.17.7.225:5000/data_delete')
    print(res.text)