from flask import Flask, jsonify, request
import json

name = "users_data.json"
users = {'user':"localhost"}

def initialize_on_start(name):
    with open(name, 'w') as outfile:
        json.dump(users, outfile)

app = Flask("__main__")

@app.route('/tests/endpoint', methods=['POST', 'GET'])
def data_appending():
    if request.method == "POST":
        input_json = request.get_json(force=True)
        f = open(name)
        current_json = json.load(f)
        f.close()
        current_json.update(input_json)
        return current_json
    else:
        return "asfgsgfd"

@app.route('/')
def index():
    with open(name, "r") as reader:
        return reader.read()

if __name__ == "__main__":
    initialize_on_start(name)
    app.run()