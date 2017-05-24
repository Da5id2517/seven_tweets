import json

from flask import Flask, request
from tweet import Tweet
from logic.storage import Storage
from config import Config


config = Config()
app = Flask(__name__)


@app.route('/tweets', methods=['GET'])
def list_tweets():
    resp = Storage().list_tweets()
    return json.dumps(resp), 200


@app.route('/tweets/<int:id>', methods=['GET'])
def get_tweet(id):
    try:
        return json.dumps(Storage().get_tweet(id)), 200
    except KeyError:
        return json.dumps({'error': 'Tweet does not exists'}), 404

@app.route('/tweets', methods=['POST'])
def post_tweet():
    name = request.form['name']
    tweet = request.form['tweet']
    id = Storage().insert_tweet(name,tweet)
    res = Tweet(id,name,tweet)
    return json.dumps(res.to_dict()), 200

@app.route('/tweets/<int:id>', methods=['DELETE'])
def delete_tweet(id):
    try:
        Storage().remove_tweet(id)
        return '', 204
    except KeyError:
        return json.dumps({'error': 'Tweet does not exist'}), 404

if __name__ == '__main__':
    app.run(host='0.0.0.0')