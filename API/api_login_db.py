import mysql.connector
from flask import Flask, request, jsonify
from mysql.connector import Error

app = Flask(__name__)


def create_connection():
    condition = None
    try:
        connection = mysql.connector.connect(
            host='localhost',
            database='python_api',
            user='root',
            password=''

        )
        if connection.is_connected():
            print("Connection established")
    except Error as e:
        print(f"Error: '{e}'")
    return connection


@app.route('/login', methods=['POST'])
def login():
    data = request.json
    username = data.get('username')
    password = data.get('password')

    if not username or not password:
        return jsonify({"message": "username or password required"}), 400

    connection = create_connection()
    cursor = connection.cursor(dictionary=True)

    cursor.execute("Select * from users where username=%s and password=%s", (username, password))
    user = cursor.fetchone()

    cursor.close()
    connection.close()

    if user:
        return jsonify({"message": "Login successful"}), 200
    else:
        return jsonify({"message": "invalid credentials"}), 401


if __name__ == "__main__":
    app.run(debug=True)
