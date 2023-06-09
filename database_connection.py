import mysql.connector
import os
# uncomment and add filepath in case of [WinError 3] The system cannot find the path
# os.chdir(<absolute path>)
database_name = "miracle_cure_biotech"


def connect_database():
    return mysql.connector.connect(
            host="localhost",
            user="root",
            password="512451245124j@D",
            database=database_name
    )


def create_database():
    db = mysql.connector.connect(
        host="localhost",
        user="root",
        password="512451245124j@D"
    )
    cursor = db.cursor()

    cursor.execute(f"SHOW DATABASES LIKE '{database_name}'")

    if not cursor.fetchone():
        cursor.execute(f"CREATE DATABASE {database_name}")

    cursor.close()
    db.close()


def create_tables():
    path = 'scripts/setup'
    sql_files = [f for f in os.listdir('scripts/setup')]
    for sql_file in sql_files:
        with open(os.path.join(path, sql_file), 'r') as file:
            sql_create = file.read().split(';')
            db = connect_database()
            mydb = db.cursor()
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

