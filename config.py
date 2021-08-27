import os


class Config:
    '''
    Parent configuration class
    '''
    SECRET_KEY = os.environ.get('SECRET_KEY')
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://moringa:7166@localhost/book'
    

    #  email configurations
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get("MAIL_USERNAME")
    MAIL_PASSWORD = os.environ.get("MAIL_PASSWORD")

    
class DevConfig(Config):
    '''
    Child configuration class

    Args:
        Config:takes the configuration child class as an argument 
    '''
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://moringa:7166@localhost/book'

    DEBUG = True


class ProdConfig(Config):
    '''
    Production configuration child class

    Args:
        Config: takes the parent configuration class as an argument
    '''
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL")
    if SQLALCHEMY_DATABASE_URI.startswith("postgres://"):
      SQLALCHEMY_DATABASE_URI= SQLALCHEMY_DATABASE_URI.replace("postgres://", "postgresql://", 1)




config_options = {
    'development': DevConfig,
    'production': ProdConfig
}
