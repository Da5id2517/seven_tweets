from logic.storage import Storage

s = Storage('test.json')

def test_insert_tweet():
    s = Storage('test.json')
    message = {'name': 'John', 'tweet': 'Hello, I\'m John.'}
    id = s.insert_tweet(message)
    assert(isinstance(id, int))
    assert(id >= 0)
