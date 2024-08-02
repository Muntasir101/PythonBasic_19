import mysql.connector

config = {
    'user': "root",
    "password": '',
    'host': 'localhost', # 127.0.0.1
    'database': 'python_mysql'
}

# establish connection
connection = mysql.connector.connect(**config)

# creating a cursor object to interact with database
cursor = connection.cursor()

# sql query to create a table
create_table_query = """
CREATE TABLE IF NOT EXISTS users(
    id INT Auto_increment NOT NULL primary key,
    name VARCHAR(255) NOT NULL,
    age INT DEFAULT NULL
    )
"""

# executing the query
cursor.execute(create_table_query)
print("Table created successfully")