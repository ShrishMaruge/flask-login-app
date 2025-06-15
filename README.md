# 🔐 Flask Login System with MySQL

A fully functional Flask-based login system with MySQL database integration. This project allows users to register, log in, and manage sessions securely using password hashing and Bootstrap-styled UI.

---

## 🌐 Live Demo

[![Deploy to Render](https://img.shields.io/badge/deployed-on--render-success?style=for-the-badge&logo=render)]([https://your-deployed-link.onrender.com](https://flask-login-app-kn5d.onrender.com))

---

## 💡 Features

- 🧾 Signup & Login with validation
- 🔐 Secure password hashing (Werkzeug)
- 💼 MySQL database integration
- 📦 Flash messaging for feedback
- 🧠 Session-based access control
- 🎨 Clean Bootstrap 5 UI
- ⚠️ Alerts for login/signup status
- 🚪 Logout functionality

---
| Login Page                      | Signup Page                       | Dashboard                     |
| ------------------------------- | --------------------------------- | ----------------------------- |
| ![Screenshot 2025-06-15 151253](https://github.com/user-attachments/assets/4a4f66b7-f8ce-4d75-9780-18dfc0aafb0b) | ![Screenshot 2025-06-15 151236](https://github.com/user-attachments/assets/17b80b65-df61-4e89-90c7-6f9f36745118) | ![Screenshot 2025-06-15 151315](https://github.com/user-attachments/assets/45cf36f1-2933-4a50-a814-1258a899efa8) |

---

## 🛠 Tech Stack

| Layer          | Technology                  |
|----------------|------------------------------|
| Framework      | Flask                        |
| Language       | Python 3                     |
| Database       | MySQL                        |
| Frontend       | HTML5, CSS3, Bootstrap 5     |
| Authentication | Werkzeug security utils      |
| Deployment     | Render / Railway / Localhost |

---

## ⚙️ Clone the repo

git clone https://github.com/ShrishMaruge/flask-login-app.git
cd flask-login-app

---

## 📦 Install dependencies

pip install -r requirements.txt

---
## 🔐 Set up .env (optional)
If you add python-dotenv, store sensitive data like this in .env:

FLASK_SECRET_KEY=supersecretkey
MYSQL_USER=root
MYSQL_PASSWORD=your_password
MYSQL_DB=Login

---

## 🗃️ MySQL Database Setup

CREATE DATABASE Login;

USE Login;

CREATE TABLE register (
    username VARCHAR(30) PRIMARY KEY,
    password VARCHAR(255)
);

---
## ⚖️ License
This project is licensed under the Apache License 2.0
© 2025 Shrish Maruge

## 🙋‍♂️ Author
Shrish Maruge
📫 Connect with me on GitHub

---

## 📂 Project Structure

```bash
flask-login-app/
├── static/
│   └── style.css
├── templates/
│   ├── base.html
│   ├── home.html
│   ├── login.html
│   └── signup.html
├── app.py
├── requirements.txt
├── .gitignore
├── LICENSE
└── README.md


