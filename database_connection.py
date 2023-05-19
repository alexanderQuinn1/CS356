import mysql.connector
import os
# uncomment and add filepath in case of [WinError 3] The system cannot find the path
# os.chdir(<absolute path>)

def connect_database(database):
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


def create_database(dbname):
    db = connect_database(None)
    create_db = db.cursor()

    create_db.execute(f"SHOW DATABASES LIKE '{dbname}'")

    if not create_db.fetchone():
        create_db.execute(f"CREATE DATABASE {dbname}")

    create_db.close()
    db.close()

    return dbname


def create_tables(dbname):
    path = 'scripts/setup'
    sql_files = [f for f in os.listdir('scripts/setup')]
    for sql_file in sql_files:
        with open(os.path.join(path, sql_file), 'r') as file:
            sql_create = file.read().split(';')
            db = connect_database(dbname)
            mydb = db.cursor()
            for sql_statement in sql_create:
                if sql_statement.strip():  # Skip empty statements
                    mydb.execute(sql_statement)
                    db.commit()
            mydb.close()
            db.close()


def create():
    database_name = "miracle_cure_biotech"
    db = create_database(database_name)
    create_tables(db)
