import os

class Config:
    QUOTES_API = 'http://quotes.stormconsultancy.co.uk/random.json'
    SECRET_KEY = '45454667ffhgfgf'
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    UPLOADED_PHOTOS_DEST ='app/static/photos'
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get("MAIL_USERNAME")
    MAIL_PASSWORD = os.environ.get("MAIL_PASSWORD")
    # simple mde  configurations
    SIMPLEMDE_JS_IIFE = True
    SIMPLEMDE_USE_CDN = True



class ProdConfig(Config):
    '''
    Pruduction configuration child class
    Args:
        Config: The parent configuration class with General configuration settings
    '''
    SQLALCHEMY_DATABASE_URI = os.environ.get("postgres://hjsbgolturrcls:83523061d532ccc7bc911f1372bcd356643929b42b5575159d1d6576ef9c1606@ec2-50-17-227-28.compute-1.amazonaws.com:5432/da4nj0bpg0390n")

class TestConfig(Config):
    '''
    Testing configuration child class
    Args:
        Config: The parent configuration class with General configuration settings 
    '''
    pass

class DevConfig(Config):
    '''
    Development configuration child class
    
    Args:
        Config: The parent configuration class with General configuration settings
    '''
    SQLALCHEMY_DATABASE_URI='postgres://hjsbgolturrcls:83523061d532ccc7bc911f1372bcd356643929b42b5575159d1d6576ef9c1606@ec2-50-17-227-28.compute-1.amazonaws.com:5432/da4nj0bpg0390n'
    DEBUG = True


config_options = {
    'development': DevConfig,
    'production': ProdConfig,
    'test': TestConfig
}