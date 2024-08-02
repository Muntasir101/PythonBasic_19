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

# check if the connection is established
if connection.is_connected():
    print("Connection established successfully")
else:
    print("Connection failed: %s" % connection.error)