import random

from flask import Flask
from flask import request
from flask import render_template
from flask import jsonify

app = Flask(__name__)

app.Command = {
    "start": "None",
    "playing": "None",
    "volume": "None"
}


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/confirm')
def confirm():
    return render_template('confirm.html')

@app.route('/_add_numbers')
def add_numbers():
    a = request.args.get('a', 0, type=int)
    b = request.args.get('b', 0, type=int)
    return jsonify(result=a + b)

@app.route('/start')
def start():
    app.Command["start"] = "True"
    print app.Command
    return jsonify(app.Command)

@app.route('/stop')
def stop():
    app.Command["start"] = "False"
    print app.Command
    return jsonify(app.Command)

@app.route('/polling')
def polling():
    print app.Command
    return jsonify(app.Command)

@app.route('/pause')
def pause():
    app.Command["playing"] = "False"
    print app.Command
    return jsonify(app.Command)

@app.route('/play')
def play():
    app.Command["playing"] = "True"
    print app.Command
    return jsonify(app.Command)

@app.route('/vup')
def vup():
    app.Command["volume"] = "+20"
    print app.Command
    return jsonify(app.Command)

@app.route('/vdown')
def vdown():
    app.Command["volume"] = "-20"
    print app.Command
    return jsonify(app.Command)

@app.route('/ack')
def ack():
    command = request.args.get('command', 0, type=str)
    app.Command[command] = "None"
    print app.Command
    return jsonify(app.Command)

if __name__ == '__main__':
    app.run(host='0.0.0.0')
