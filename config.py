class Config(object):

    DEBUG = False
    TESTING = False
    SECRET_KEY = 'hard secret key!'

    # DATBASE
    SQLALCHEMY_DATABASE_URI = 'postgres://fwpghhxxgxhvze:dbd3620e516a0e9871a2f3e1b6309275d2efae750370dc44597681c05955a5' \
                              '63@ec2-23-20-70-32.compute-1.amazonaws.com:5432/ddbssoq6mokud1'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

class ProductionConfig(Config):
    pass

class DevelopmentConfig(Config):

    DEBUG = True

    #DATABASE
    #SQLALCHEMY_DATABASE_URI = "postgres://postgres:Gloyane@160298@localhost:5432/makkidb"

    # DATABASE VARIABLES
    DB_HOST = 'localhost'
    DB_NAME = 'makkidb'
    DB_USER = 'postgres'
    DB_PASSWORD = 'Gloyane@160298'
    DB_PORT = 5432

    # Mail
    MAIL_SERVER = 'smtp.gmail.com'
    MAIL_PORT = 465
    MAIL_USE_TLS = False
    MAIL_USE_SSL = True
    MAIL_USERNAME = 'rayanemakki98@gmail.com'
    MAIL_PASSWORD = 'halamadrid.m12'

    UPLOAD_EXTENSIONS = ['.jpg', '.png', 'gif']
    MAX_CONTENT_LENGTH = 1024 * 1024
    UPLOAD_PATH = 'uploads'


class TestingConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = "postgres://postgres:Gloyane@160298@localhost:5432/makkidb"