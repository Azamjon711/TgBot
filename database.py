import psycopg2 as psql
import os
from dotenv import load_dotenv
load_dotenv()


class Database:
    @staticmethod
    def connect(query, queryType):
        database = psql.connect(
            database='database',
            user='postgres',
            host='localhost',
            password='password'
        )

        cursor = database.cursor()
        cursor.execute(query)

        if queryType == "insert":
            database.commit()
            return "inserted"
        elif queryType == "select":
            return cursor.fetchall()
