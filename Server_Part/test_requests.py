import json
import requests
dictToSend = {"gay":'me'}
res = requests.post('http://127.0.0.1:5000/tests/endpoint', json=dictToSend)
print(res.text)
#dictFromServer = res.json()