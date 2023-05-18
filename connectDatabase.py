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
        miracle_cure_biotech_db = mysql.connector.connect(
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

    createDB.execute(f"SHOW DATABASES LIKE '{dbname}'")

    if createDB.fetchone():
        print(f"Database {dbname} already exists, please try again.")
    else:

        createDB.execute(f"CREATE DATABASE {dbname}")

    createDB.close()
    db.close()

    return dbname


def create_tables(dbname):
    path = "scripts/db-setup"
    sql_files = [f for f in os.listdir(path) if f.endswith('.sql')]
    for sql_file in sql_files:
        with open(os.path.join(path, sql_file), 'r') as file:
            sql_create = file.read().split(';')
            db = connectDatabase(dbname)
            mydb = db.cursor()
            for sql_statement in sql_create:
                if sql_statement.strip():  # Skip empty statements
                    mydb.execute(sql_statement)
                    db.commit()
            mydb.close()
            db.close()


database_name = "miracle_cure_biotech"
db = createdatabase(database_name)
print(db)
create_tables(db)
