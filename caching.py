```python
import redis
import os

# Redis client
cache = redis.Redis(host=os.getenv('REDIS_HOST', 'localhost'), port=os.getenv('REDIS_PORT', 6379), db=0)

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
```
