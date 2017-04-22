import json

from flask import Flask, request

from logic.storage import Storage


storage = Storage('storage.json')
app = Flask(__name__)


@app.route('/tweets', methods=['GET'])
def list_tweets():
    resp = [tweet for id,tweet in storage.list_tweets().items()]
    return json.dumps(resp), 200


@app.route('/tweets/<int:id>', methods=['GET'])
def get_tweet(id):
    try:
        return json.dumps(storage.get_tweet(id)), 200
    except KeyError:
        return json.dumps({'error': 'Tweet does not exists'}), 404

@app.route('/tweets', methods=['POST'])
def post_tweet():
    tweet_dict = {'name': request.form['name'], 'tweet': request.form['tweet']}
    new_id = storage.insert_tweet(tweet_dict)
    tweet_dict.update({'id': new_id})
    return json.dumps(tweet_dict), 200

@app.route('/tweets/<int:id>', methods=['DELETE'])
def delete_tweet(id):
    try:
        storage.remove_tweet(id)
        return '', 204
    except KeyError:
        return json.dumps({'error': 'Tweet does not exist'}), 404

if __name__ == '__main__':
    app.run(host='0.0.0.0')