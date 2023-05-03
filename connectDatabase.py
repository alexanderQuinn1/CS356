import mysql.connector
import os


def connectDatabase(database):
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


def createdatabase(dbname):
    db = connectDatabase(None)
    createDB = db.cursor()
    dbname = dbname
    createDB.execute(f"CREATE  DATABASE {dbname}")
    db.close()
    return dbname


def create_tables(dbname):
    sql_files = [f for f in os.listdir() if f.endswith('.sql')]
    for sql_file in sql_files:
        with open(sql_file, 'r') as file:
            sql_create = file.read()
            db = connectDatabase(dbname)
            mydb = db.cursor()
            mydb.execute(sql_create)
            mydb.close()
            db.close()


database_name = "miracle_cure_biotech"
db = createdatabase(database_name)
print(db)
create_tables(db)
