"""
Copyright (C) 2023 SE23-Team44
 
Licensed under the MIT License.
See the LICENSE file in the project root for the full license information.
"""

class Config(object):
    DEBUG = False
    TESTING = False
    EMAIL_PASS = 'amkx fedi ilnm qahn'
    CLIENT_ID = 'REPLACE_WITH_CLIENT_ID'
    CLIENT_SECRET = 'REPLACE_WITH_CLIENT_SECRET'
    SECRET_KEY = 'asdsdfsdfs13sdf_df%&'

class ProductionConfig(Config):
    pass

class DevelopmentConfig(Config):
    Debug = True

class TestingConfig(Config):
    TESTING = True