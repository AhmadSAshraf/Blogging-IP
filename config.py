import os

class Config:

    QUOTES_API = 'http://quotes.stormconsultancy.co.uk/random.json'
    SECRET_KEY = os.environ.get('45454667ffhgfgf')
    SECRET_KEY = os.urandom(32)
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://adminpb:root@localhost/pb'
    UPLOADED_PHOTOS_DEST ='app/static/photos'
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get("MAIL_USERNAME")
    MAIL_PASSWORD = os.environ.get("MAIL_PASSWORD")
    SIMPLEMDE_JS_IIFE = True
    SIMPLEMDE_USE_CDN = True
class ProdConfig(Config):
     SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL") 


class TestConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://adminpb:root@localhost/pb_test'

class DevConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'postgres://hjsbgolturrcls:83523061d532ccc7bc911f1372bcd356643929b42b5575159d1d6576ef9c1606@ec2-50-17-227-28.compute-1.amazonaws.com:5432/da4nj0bpg0390n'
    DEBUG = True

config_options = {
'development':DevConfig,
'production':ProdConfig,
'test':TestConfig
}
