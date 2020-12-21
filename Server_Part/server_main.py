from flask import Flask, jsonify, request
import json

name = "users_data.json"

def rewrite_database(updated):
    with open(name, 'w') as outfile:
        json.dump(updated, outfile)

app = Flask("__main__")

@app.route('/data', methods=['POST', 'GET'])
def data_appending():
    f = open(name)
    current_json = json.load(f)
    f.close()
    if request.method == "POST":
        input_json = request.get_json(force=True)
        current_json['users'].append(input_json)
        rewrite_database(current_json)
        return str(current_json)
    else:
        return str(current_json)

@app.route('/')
def index():
    with open(name, "r") as reader:
        return reader.read()

if __name__ == "__main__":
    app.run(host = '192.168.43.84',debug=True)