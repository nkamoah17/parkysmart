from itsdangerous import TimedJSONWebSignatureSerializer as Serializer
from itsdangerous import BadSignature, SignatureExpired

SECRET_KEY = "YOUR_SECRET_KEY"  # Replace with your secret key

def generate_key():
    """
    Generate a secure API key using itsdangerous library
    """
    s = Serializer(SECRET_KEY, expires_in=3600)
    return s.dumps({'api_key': 'secure_key'}).decode()

def validate_key(api_key):
    """
    Validate an API key using itsdangerous library. This function checks
    the provided API key against the generated secure key.
    """
    s = Serializer(SECRET_KEY)
    try:
        data = s.loads(api_key)
    except SignatureExpired:
        return False  # valid token, but expired
    except BadSignature:
        return False  # invalid token
    return True
