#!/usr/bin/env python
import bottle
import bottle.ext.redis

from settings import REDIS_DB_CONF

import os.path

APP_DIR = os.path.abspath(os.path.dirname(__file__))

bottle.TEMPLATE_PATH.append( os.path.join(APP_DIR, 'views'))

uploader = bottle.Bottle()
redis = bottle.ext.redis.RedisPlugin(**REDIS_DB_CONF)

uploader.install(redis)

