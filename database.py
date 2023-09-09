import psycopg2
from psycopg2 import pool
from config import get_config

class Database:
    """
    Database class. This class will handle all the database operations.
    """
    def __init__(self):
        self.config = get_config()
        self.db_pool = None

    def init_app(self):
        """
        Initialize the database connection pool.
        """
        self.db_pool = pool.SimpleConnectionPool(
            1, 20,
            host=self.config.DB_HOST,
            database=self.config.DB_NAME,
            user=self.config.DB_USER,
            password=self.config.DB_PASSWORD
        )

    def get_conn(self):
        """
        Get a connection from the pool.
        """
        return self.db_pool.getconn()

    def put_conn(self, conn):
        """
        Return a connection to the pool.
        """
        self.db_pool.putconn(conn)

    def execute_query(self, query, params):
        """
        Execute a query and return the result.
        """
        conn = self.get_conn()
        try:
            with conn.cursor() as cur:
                cur.execute(query, params)
                result = cur.fetchone()
                return result[0] if result else None
        finally:
            self.put_conn(conn)

    def execute_update(self, query, params):
        """
        Execute an update query.
        """
        conn = self.get_conn()
        try:
            with conn.cursor() as cur:
                cur.execute(query, params)
            conn.commit()
        finally:
            self.put_conn(conn)

db = Database()

def get_db():
    """
    Returns the database object
    """
    return db
