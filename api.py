from itsdangerous import TimedJSONWebSignatureSerializer as Serializer
from itsdangerous import BadSignature, SignatureExpired
from flask import request, abort

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
        if 'api_key' in data and data['api_key'] == 'secure_key':
            return True
    except SignatureExpired:
        return False  # valid token, but expired
    except BadSignature:
        return False  # invalid token
    return False

def api_key_required(f):
    """
    A decorator to ensure that the API key is provided in the request
    """
    @wraps(f)
    def decorated_function(*args, **kwargs):
        api_key = request.headers.get('API-Key')
        if not api_key or not validate_key(api_key):
            abort(401)
        return f(*args, **kwargs)
    return decorated_function
