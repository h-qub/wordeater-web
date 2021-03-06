# -*- coding: utf-8 -*-
import os
from configparser2 import RawConfigParser

__author__ = 'Glebov Boris'


ENVELOPE_DATA = "data"
PROJECT_DIR = os.path.abspath(os.path.dirname(__file__))

config = RawConfigParser()
config.read('{0}/settings.ini'.format(PROJECT_DIR))

SECRET_KEY = '\2\1flsdfldsfoglsfo33fdsafs\1\2\e\y\y\h'

#
# Версия
#
version = config.get('APPLICATION', 'version')

#
# API
API_PATH = '/api/v1'
API_USER_AGENT = 'Wordeater/1.0'

# MongoDB
DATABASE = {
    'host': config.get('DATABASE', 'host'),
    'port': config.get('DATABASE', 'port'),
    'db_name': config.get('DATABASE', 'db_name')
}

# [MEMCACHED]
MEMCACHED = {
    'host': config.get('MEMCACHED', 'host'),
    'port': config.get('MEMCACHED', 'port')
}

# [LOGGER]
LOG_PATH = config.get('LOGGER', 'directory')

# [APPLICATION]
CARDS_IN_GROUP_AMOUNT = int(config.get('APPLICATION', 'cards_in_group_amount'))
SESSION_EXPIRES = int(config.get('APPLICATION', 'session_expires'))
IS_DEBUG = int(config.get('APPLICATION', 'is_debug')) == 1

# [TRANSLATE_YANDEX_PROVIDER]
TRANSLATE_YANDEX_KEY = config.get('TRANSLATE_YANDEX_PROVIDER', 'key')

# [BLUEMIX]
BLUEMIX_SYNTH_URL = config.get('BLUEMIX_SYNTH_PROVIDER', 'url')
BLUEMIX_SYNTH_USERNAME = config.get('BLUEMIX_SYNTH_PROVIDER', 'username')
BLUEMIX_SYNTH_PASSWORD = config.get('BLUEMIX_SYNTH_PROVIDER', 'password')
