import mysql.connector
from mysql.connector import Error
from config import Config

def get_db_connection():
    try:
        connection = mysql.connector.connect(
            host=Config.DB_HOST,
            user=Config.DB_USER,
            password=Config.DB_PASSWORD,
            database=Config.DB_NAME,
            port=Config.DB_PORT,
            connection_timeout=30,       # Connection timeout in seconds
            autocommit=False             # Manual commit control
        )

        if connection.is_connected():
            return connection

    except Error as e:
        print("Dataset connection error:", e)
        return None
