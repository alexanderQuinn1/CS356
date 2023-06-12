import mysql.connector
import os

DB_NAME = "miracle_cure_biotech"
HOST = "localhost"
USER = "root"
PASSWORD = "512451245124j@D"


def connect_database():
    return mysql.connector.connect(
            host=HOST,
            user=USER,
            password=PASSWORD,
            database=DB_NAME
    )


def create_database():
    db = mysql.connector.connect(
        host=HOST,
        user=USER,
        password=PASSWORD
    )
    cursor = db.cursor()

    cursor.execute(f"SHOW DATABASES LIKE '{DB_NAME}'")

    if not cursor.fetchone():
        cursor.execute(f"CREATE DATABASE {DB_NAME}")

    cursor.close()
    db.close()


def create_tables():
    path = 'scripts/setup'
    sql_files = [f for f in os.listdir('scripts/setup')]
    db = connect_database()
    mydb = db.cursor()
    for sql_file in sql_files:
        with open(os.path.join(path, sql_file), 'r') as file:
            sql_create = file.read().split(';')
            for sql_statement in sql_create:
                if sql_statement.strip():
                    mydb.execute(sql_statement)
                    db.commit()
    mydb.close()
    db.close()


def create():
    create_database()
    create_tables()


def execute_update(query_string, params):
    db = connect_database()
    cursor = db.cursor()

    cursor.execute(query_string, params)
    db.commit()

    cursor.close()
    db.close()


def execute_fetch(query_string, params = None):
    db = connect_database()
    cursor = db.cursor()

    cursor.execute(query_string, params)
    results = cursor.fetchall()

    cursor.close()
    db.close()
    return results
