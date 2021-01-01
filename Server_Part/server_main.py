from flask import Flask, jsonify, request
import json

name = "users_data.json"

def rewrite_database(updated):
    with open(name, 'w') as outfile:
        json.dump(updated, outfile)

app = Flask("__main__")

@app.route('/data_append', methods=['POST', 'GET'])
def data_append():
    f = open(name)
    current_json = json.load(f)
    f.close()
    if request.method == "POST":
        input_json = request.get_json()
        current_json['users'].append(input_json)
        rewrite_database(current_json)
        return str(current_json)
    if request.method == "GET":
        return str(current_json)       
@app.route('/data_delete', methods = ['DELETE'])
def data_delete():
    f = open(name)
    current_json = json.load(f)
    f.close()
    user_ip = str(request.remote_addr)
    for i in range(len(current_json['users'])):
        if current_json['users'][i]['ip'] == user_ip:
            del current_json['users'][i]
            break
    rewrite_database(current_json)
    return str(current_json)    
@app.route('/')
def index():
    with open(name, "r") as reader:
        return reader.read()


if __name__ == "__main__":
    app.run(host = '0.0.0.0', port= 5000)