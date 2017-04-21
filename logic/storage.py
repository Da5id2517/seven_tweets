import json
from json import JSONDecodeError


class Storage(object):

    def __init__(self, file_path):
        self._file_path = file_path
        try:
            f = open(self._file_path, 'r')
            content = json.load(f)

            tmp_dict = {}
            for item in content:
                tmp_dict[int(item)] = content[item]
            self._tweets = tmp_dict
            f.close()
        except (JSONDecodeError, FileNotFoundError) as e:
            self._tweets = {}
            f = open(self._file_path, 'w')
            json.dump(self._tweets, f)
            f.close()

    def insert_tweet(self, message):
        try:
            new_id = max(self._tweets.keys()) + 1
        except ValueError:
            new_id = 0
        self._tweets[new_id] = {'id': new_id, 'name': message['name'], 'tweet': message['tweet']}
        self.persist()
        return new_id

    def remove_tweet(self, id):
        self._tweets.pop(id)
        self.persist()

    def persist(self):
        f = open(self._file_path, 'w')
        json.dump(self._tweets, f)
        f.close()

    def list_tweets(self):
        return self._tweets

    def get_tweet(self, id):
        return self._tweets[id]
