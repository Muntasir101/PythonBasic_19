from flask import Flask, request, jsonify

app = Flask(__name__)

users = {
    "user1": "123456",
    "user2": "123456"
}


@app.route('/login', methods=['POST'])
def login():
    data = request.json
    username = data.get('username')
    password = data.get('password')

    if not username or not password:
        return jsonify({"message": "username or password required"}), 400
    if username in users and users[username] == password:
        return jsonify({"message": "Login successful"}), 200
    else:
        return jsonify({"message": "Invalid username or password"}), 401


if __name__ == "__main__":
    app.run(debug=True)
