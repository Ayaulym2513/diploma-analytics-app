import os
from pymongo import MongoClient
import pymysql

# Подключение к MySQL (порт 3307)
MYSQL_HOST = "localhost"
MYSQL_PORT = 3307
MYSQL_USER = "root"
MYSQL_PASSWORD = "rootpassword"
MYSQL_DB = "analytics_db"

def get_mysql_connection():
    connection = pymysql.connect(
        host=MYSQL_HOST,
        port=MYSQL_PORT,
        user=MYSQL_USER,
        password=MYSQL_PASSWORD,
        database=MYSQL_DB,
        cursorclass=pymysql.cursors.DictCursor
    )
    return connection

# Подключение к MongoDB
MONGO_URI = "mongodb://localhost:27017/"
mongo_client = MongoClient(MONGO_URI)
mongo_db = mongo_client["analytics_bigdata"]
logs_collection = mongo_db["system_logs"]

print("Модуль базы данных успешно настроен!")
