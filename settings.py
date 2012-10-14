import os.path

PROJECT_DIR = os.path.abspath(os.path.dirname(__file__))

MEDIA_ROOT = os.path.join(PROJECT_DIR, 'uploads/')

STATIC_ROOT = os.path.join(PROJECT_DIR, 'static/')

REDIS_DB_CONF = {
        'host'       : 'localhost',
        'port'       : 6379,
        'database'   : 0,
}


