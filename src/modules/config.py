class Config(object):
    DEBUG = False
    TESTING = False
    EMAIL_PASS = 'PUT_YOUR_PASSWORD_HERE'
    CLIENT_ID = 'REPLACE_WITH_CLIENT_ID'
    CLIENT_SECRET = 'REPLACE_WITH_CLIENT_SECRET'

class ProductionConfig(Config):
    pass

class DevelopmentConfig(Config):
    Debug = True

class TestingConfig(Config):
    TESTING = True