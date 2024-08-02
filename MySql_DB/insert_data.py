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
insert_query = "INSERT INTO users (name,age) VALUES (%s,%s)"
data = [
    ("smith", 20),
    ("Alice", 30),
    ("Bob", 40)
]

# executing the query
cursor.executemany(insert_query, data)
connection.commit()
print("Data insert successfully")
