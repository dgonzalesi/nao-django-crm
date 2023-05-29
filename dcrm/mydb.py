# IMPORT THE CONECTOR TO DB IN POSTGRESQL AND THE LIBRARY TO WORK WITH DATETIME

import os
import psycopg2

database = psycopg2.connect(
    host = os.environ['DB_HOSTS'],
    user = os.environ['DB_USERNAME'],
    dbaname = os.environ['DB_NAME'],
    password = os.environ['DB_PASSWORD']
)

# Open a curso to perform database operations

cursor = database.cursor()

# Execute a command: this creates a new table

#  cursos.excute("CREATE DATABES IF NOT EXISTS django_nao_crm;")
# cursor.execute("CREATE TABLE IF NOT EXISTS customers (id serial PRIMARY KEY, name varchar(255), email varchar(255), phone varchar(255), date timestamp);")

# Execute a query
# cursor.execute("SELECT * FROM customers;")

# retrive query results
# records = cursor.fetchall()

print("ALL DONE")
