from flask import Flask, request, jsonify

app = Flask(__name__)

# Temporary in-memory user list
users = []

@app.route('/')
def home():
    return "Welcome to the API! Use /users"

# Get all users
@app.route('/users', methods=['GET'])
def get_users():
    return jsonify(users)

# Add a new user
@app.route('/users', methods=['POST'])
def add_user():
    data = request.get_json()
    users.append(data)
    return jsonify({"message": "User added successfully"}), 201

# Get user by ID
@app.route('/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    for user in users:
        if user["id"] == user_id:
            return jsonify(user)
    return jsonify({"error": "User not found"}), 404

# Update user by ID
@app.route('/users/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    data = request.get_json()
    for user in users:
        if user["id"] == user_id:
            user.update(data)
            return jsonify({"message": "User updated successfully"})
    return jsonify({"error": "User not found"}), 404

# Delete user by ID
@app.route('/users/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    for i, user in enumerate(users):
        if user["id"] == user_id:
            users.pop(i)
            return jsonify({"message": "User deleted successfully"})
    return jsonify({"error": "User not found"}), 404

if __name__ == '__main__':
    app.run(debug=True)

