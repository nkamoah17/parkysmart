```python
import os

class Config:
    """
    Configuration class. This class will hold all the configuration variables for our application.
    """
    # Flask settings
    FLASK_DEBUG = os.getenv('FLASK_DEBUG', False)

    # Database settings
    DB_HOST = os.getenv('DB_HOST', 'localhost')
    DB_NAME = os.getenv('DB_NAME', 'parking_lot')
    DB_USER = os.getenv('DB_USER', 'postgres')
    DB_PASSWORD = os.getenv('DB_PASSWORD', 'password')

    # S3 settings
    S3_BUCKET = os.getenv('S3_BUCKET', 'mybucket')
    S3_ACCESS_KEY = os.getenv('S3_ACCESS_KEY', '')
    S3_SECRET_KEY = os.getenv('S3_SECRET_KEY', '')

    # Redis settings
    REDIS_HOST = os.getenv('REDIS_HOST', 'localhost')
    REDIS_PORT = os.getenv('REDIS_PORT', 6379)

    # Model settings
    MODEL_PATH = os.getenv('MODEL_PATH', 'model.pth')

    # API settings
    API_KEY = os.getenv('API_KEY', '')

def get_config():
    """
    Returns the configuration object
    """
    return Config
```
