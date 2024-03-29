import json
from flask import Flask, jsonify


app = Flask(__name__)

@app.route('/')
def hello_world():
    res = {"msg": "Endpoint success"}
    return jsonify(res)


if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port=5000)
