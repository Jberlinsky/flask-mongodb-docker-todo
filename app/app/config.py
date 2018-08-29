import os


class Config(object):
    DEBUG = False
    TESTING = False
    CRSF_ENABLED = True
    MONGO_URI = "mongodb://localhost:27017/todos"


class DockerConfig(Config):
    DEBUG = False
    MONGO_URI = os.environ['MONGO_URI']
