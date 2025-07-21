🛠️ How to Use This Flask API
Install Flask

pip install flask

Run the App

python app.py

API Endpoints (Use Postman):

GET /users → Get all users

<img width="1920" height="1080" alt="Screenshot (43)" src="https://github.com/user-attachments/assets/637e7ef8-8d04-40f1-8402-c1ab5cb02af9" />

POST /users → Add a user

json
Copy
Edit
{
  "id": 1,
  "name": "Divyasha",
  "email": "divyasha@example.com"
}
<img width="1920" height="1080" alt="Screenshot (44)" src="https://github.com/user-attachments/assets/8b40302f-520d-4d46-b18f-767ab4c8b90c" />

GET /users/<id> → Get user by ID
<img width="1920" height="1080" alt="Screenshot (45)" src="https://github.com/user-attachments/assets/f4f37772-2934-4b42-a924-6734fc82eade" />


PUT /users/<id> → Update user
<img width="1920" height="1080" alt="Screenshot (46)" src="https://github.com/user-attachments/assets/482534d1-b3ee-4b5f-8abe-1f479e4e300d" />


DELETE /users/<id> → Delete user

Base URL:
http://127.0.0.1:5000
