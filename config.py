import os
import configparser

class Config:
    """
    Configuration class. This class will hold all the configuration variables for our application.
    """
    config = configparser.ConfigParser()
    config.read('default_config.ini')

    # Flask settings
    FLASK_DEBUG = os.getenv('FLASK_DEBUG', config.get('Flask', 'FLASK_DEBUG', fallback=False))

    # Database settings
    DB_HOST = os.getenv('DB_HOST', config.get('Database', 'DB_HOST', fallback='localhost'))
    DB_NAME = os.getenv('DB_NAME', config.get('Database', 'DB_NAME', fallback='parking_lot'))
    DB_USER = os.getenv('DB_USER', config.get('Database', 'DB_USER', fallback='postgres'))
    DB_PASSWORD = os.getenv('DB_PASSWORD', config.get('Database', 'DB_PASSWORD', fallback='password'))

    # S3 settings
    S3_BUCKET = os.getenv('S3_BUCKET', config.get('S3', 'S3_BUCKET', fallback='mybucket'))
    S3_ACCESS_KEY = os.getenv('S3_ACCESS_KEY', config.get('S3', 'S3_ACCESS_KEY', fallback=''))
    S3_SECRET_KEY = os.getenv('S3_SECRET_KEY', config.get('S3', 'S3_SECRET_KEY', fallback=''))

    # Redis settings
    REDIS_HOST = os.getenv('REDIS_HOST', config.get('Redis', 'REDIS_HOST', fallback='localhost'))
    REDIS_PORT = os.getenv('REDIS_PORT', config.get('Redis', 'REDIS_PORT', fallback=6379))

    # Model settings
    MODEL_PATH = os.getenv('MODEL_PATH', config.get('Model', 'MODEL_PATH', fallback='model.pth'))

    # API settings
    API_KEY = os.getenv('API_KEY', config.get('API', 'API_KEY', fallback=''))

def get_config():
    """
    Returns the configuration object
    """
    return Config
