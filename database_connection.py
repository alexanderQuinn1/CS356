import mysql.connector
import os


def connect_database(database):
    if database is None:
        miracle_cure_biotech_db = mysql.connector.connect(
            host="localhost",
            user="root",
            password="512451245124j@D"
        )
    else:
        miracle_cure_biotech_db  = mysql.connector.connect(
            host="localhost",
            user="root",
            password="512451245124j@D",
            database=database
        )

    return miracle_cure_biotech_db


def create_database(dbname):
    db = connect_database(None)
    createDB = db.cursor()
    dbname = dbname
    createDB.execute(f"CREATE  DATABASE {dbname}")
    db.close()
    return dbname


def create_tables(dbname):
    sql_files = [f for f in os.listdir('scripts/setup')]
    for sql_file in sql_files:
        with open(sql_file, 'r') as file:
            sql_create = file.read()
            db = connect_database(dbname)
            mydb = db.cursor()
            mydb.execute(sql_create)
            mydb.close()
            db.close()


def create():
    database_name = "miracle_cure_biotech"
    db = create_database(database_name)
    create_tables(db)
