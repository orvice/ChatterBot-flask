from flask import Flask
from flask import json, request
import bot
import config

app = Flask(__name__)


@app.route("/", methods=['GET', 'POST'])
def ask():
    msg = request.form['msg']
    resp = bot.talk(msg)
    print(resp)
    data = {
        'resp': "%s" % resp
    }
    response = app.response_class(
        response=json.dumps(data),
        status=200,
        mimetype='application/json'
    )
    return response

@app.route("/train", methods=['GET', 'POST'])
def hello():
    in = request.form['input']
    res = request.form['res']
    resp = bot.train(in,res)
    data = {
        'resp': "%s" % resp
    }
    response = app.response_class(
        response=json.dumps(data),
        status=200,
        mimetype='application/json'
    )
    return response


if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True, port=config.port)
