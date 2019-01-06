import os


def read_secret_key():
    with open(os.environ.get('SECRET_KEY_FILE'), 'rt') as f:
        return f.read()
    raise RuntimeError('cannot read SECRET_KEY_FILE')


class Config(object):
    SECRET_KEY = read_secret_key()
    MONGO_HOST = os.environ.get('MONGO_HOST', 'mongo')
    MONGO_DBNAME = os.environ.get('MONGO_DBNAME', 'appname')
    MONGO_URI = f'mongodb://{MONGO_HOST}:27017/{MONGO_DBNAME}'

    _redis_url = 'redis://:{}@{}:6379/1'.format(
        os.environ.get('REDIS_PASSWORD', ''),
        os.environ.get('REDIS_HOST', 'redis'))

    BROKER_URL = _redis_url
    CELERY_RESULT_BACKEND = _redis_url
    CELERY_TIMEZONE = 'Asia/Seoul'


class ConfigDebug(Config):
    SECRET_KEY = 'develop secret key'
    DEBUG = True

