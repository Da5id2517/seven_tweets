import pg8000,functools
from tweet import Tweet
from config import Config


def uses_db(f):
    @functools.wraps(f)
    def wrapper(cls,*args,**kwargs):
        cursor = cls._conn.cursor()
        res = f(cls,cursor,*args,**kwargs)
        cursor.close()
        cls._conn.commit()
        return res
    return wrapper


class Storage(object):
    _conn = pg8000.connect(**Config.DB_CONFIG)

    @classmethod
    @uses_db
    def insert_tweet(cls, cursor, name, tweet):
        cursor.execute("INSERT INTO tweets (name,tweet) VALUES (%s,%s) RETURNING id", (name, tweet))
        return cursor.fetchone()[0]

    @classmethod
    @uses_db
    def remove_tweet(cls, cursor, id):
        cursor.execute("DELETE FROM tweets WHERE id = (%s)", (id,))

    @classmethod
    @uses_db
    def list_tweets(cls, cursor,):
        cursor.execute("SELECT id,name,tweet FROM tweets")
        res = [Tweet(*data).to_dict() for data in cursor.fetchall()]
        return res

    @classmethod
    @uses_db
    def get_tweet(cls, cursor, id):
        cursor.execute("SELECT id, name, tweet FROM tweets WHERE id=%s", (id,))
        res = Tweet(*cursor.fetchone()).to_dict()
        return res