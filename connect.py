import os
import mysql.connector
from dotenv import load_dotenv

load_dotenv()

DB_HOST = os.getenv('DB_HOST')
DB_DATABASE = os.getenv('DB_DATABASE')
DB_USERNAME = os.getenv('DB_USERNAME')
DB_PASSWORD = os.getenv('DB_PASSWORD')

API_KEY = os.getenv('API_KEY')

print(DB_HOST)

config = {
  'user': DB_USERNAME,
  'password': DB_PASSWORD,
  'host': DB_HOST,
  'unix_socket': '/Applications/MAMP/tmp/mysql/mysql.sock',
  'database': DB_DATABASE,
  'raise_on_warnings': True
}

cnx = mysql.connector.connect(**config)

cnx.close()