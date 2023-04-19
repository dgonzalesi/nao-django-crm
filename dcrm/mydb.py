# IMPORT THE CONECTOR TO DB IN POSTGRESQL AND THE LIBRARY TO WORK WITH DATETIME

import psycopg2

database = psycopg2.connect(
    host = "localhost",
    user = "postgres",
    dbaname = "django_nao_crm",
    password = "12345678"
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
