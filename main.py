from flask import Flask, request, jsonify
import json
import random

with open('lists.json', 'r', encoding='UTF8') as f:
    data = json.load(f)

app = Flask(__name__)

@app.route('/getText')
def getText():
    rT = RandText()
    return jsonify({"Text": rT})

def RandText():
    #61
    r = random.randrange(0, 50)
    return data["List"][r]

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5555)