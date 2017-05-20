import os


class Config(object):
    DB_CONFIG = dict(user=os.environ.get('ST_DB_USER', 'radionica'),
                     database=os.environ.get('ST_DB_NAME', 'radionica'),
                     host=os.environ.get('ST_DB_HOST', 'localhost'),
                     password=os.environ.get('ST_DB_PASS', 'P4ss'),
                     port=int(os.environ.get('ST_DB_PORT', '5431')))