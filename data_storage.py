import uuid
from werkzeug.utils import secure_filename
from psycopg2 import pool, extras
import boto3

# Database connection pool
db_pool = None

# S3 client
s3 = boto3.client('s3')

def init_app(app):
    """
    Initialize the data storage module with the given Flask app.
    """
    global db_pool
    db_pool = pool.SimpleConnectionPool(
        minconn=1, 
        maxconn=20,
        host=app.config['DB_HOST'],
        database=app.config['DB_NAME'],
        user=app.config['DB_USER'],
        password=app.config['DB_PASSWORD']
    )
    # Initialize the S3 client
    global s3
    s3 = boto3.client('s3')

def save_file(file):
    """
    Save a file to S3 and return its ID.
    """
    file_id = str(uuid.uuid4())
    filename = secure_filename(file.filename)
    s3.upload_fileobj(file, 'mybucket', f'{file_id}/{filename}')
    return file_id

def get_file(file_id):
    """
    Retrieve a file from S3.
    """
    filename = secure_filename(file_id)
    file_obj = s3.get_object(Bucket='mybucket', Key=f'{file_id}/{filename}')
    return file_obj['Body'].read()

def save_metadata(file_id, occupancy):
    """
    Save metadata to the database.
    """
    if db_pool is None:
        raise Exception("Database connection pool is not initialized. Call init_app(app) first.")
    conn = db_pool.getconn()
    try:
        with conn, conn.cursor() as cur:
            cur.execute(
                'INSERT INTO occupancy (file_id, occupancy) VALUES (%s, %s)',
                (file_id, occupancy)
            )
    finally:
        db_pool.putconn(conn)

def get_metadata(file_id):
    """
    Retrieve metadata from the database.
    """
    if db_pool is None:
        raise Exception("Database connection pool is not initialized. Call init_app(app) first.")
    conn = db_pool.getconn()
    try:
        with conn, conn.cursor() as cur:
            cur.execute(
                'SELECT occupancy FROM occupancy WHERE file_id = %s',
                (file_id,)
            )
            result = cur.fetchone()
            return result[0] if result else None
    finally:
        db_pool.putconn(conn)


