
import redis
from config import get_config

# Get the configuration
config = get_config()

# Redis client
cache = redis.Redis(host=config.REDIS_HOST, port=config.REDIS_PORT, db=0)

def save(key, value):
    """
    Save a value to the cache.
    """
    cache.set(key, value)

def get(key):
    """
    Retrieve a value from the cache.
    """
    return cache.get(key)

def delete(key):
    """
    Delete a value from the cache.
    """
    cache.delete(key)
