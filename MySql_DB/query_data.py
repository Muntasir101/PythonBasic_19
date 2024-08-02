import mysql.connector

config = {
    'user': "root",
    "password": '',
    'host': 'localhost',  # 127.0.0.1
    'database': 'python_mysql'
}

# establish connection
connection = mysql.connector.connect(**config)

# creating a cursor object to interact with database
cursor = connection.cursor()

# sql query to create a table
select_query = "Select * from users"

# executing the query
cursor.execute(select_query)

# fetch all rows
rows = cursor.fetchall()

# display the data
for row in rows:
    print(row)