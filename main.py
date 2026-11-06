import dotenv
import os
import psycopg
from psycopg.rows import dict_row

class Database:
    def __init__(self):
        dotenv.load_dotenv()
        self.connection = psycopg.connect(
            dbname=os.getenv('DB_NAME'),
            user=os.getenv('DB_USER'),
            password=os.getenv('DB_PASSWORD'),
            host=os.getenv('DB_HOST'),
            port=os.getenv('DB_PORT'),
            row_factory=dict_row
        )
