## Visitor Management System (Flask + MySQL)

A simple **Visitor Management Web Application** built using **Flask (Python)** and **MySQL**. This project allows users to add, view, edit, and delete visitor records with authentication.

---

## 🚀 Features

* 🔐 Login system (basic authentication)
* ➕ Add new visitors
* ✏️ Edit visitor details
* ❌ Delete visitors
* 📋 View all visitor records in a dashboard
* 🎨 Clean UI using HTML + CSS
* 🗄️ MySQL database integration

---

## 🛠️ Tech Stack

* **Backend:** Python, Flask
* **Frontend:** HTML, CSS
* **Database:** MySQL
* **Libraries:**

  * Flask
  * mysql-connector-python

---

## 📁 Project Structure

```
visitor_app/
│
├── app.py                # Main Flask app
├── db.py                 # Database connection file
├── requirements.txt      # Python dependencies
│
├── templates/             # HTML templates
│   ├── index.html          # Dashboard page
│   ├── login.html          # Login page
│   ├── add.html            # Add visitor page
│   ├── edit.html           # Edit visitor page
│
├── static/
│   └── style.css           # CSS styles
│
└── README.md
```

---

## ⚙️ Setup & Installation

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/your-username/visitor_app.git
cd visitor_app
```

### 2️⃣ Create Virtual Environment (Optional but Recommended)

```bash
python -m venv venv
# Activate
source venv/bin/activate   # Linux/Mac
venv\\Scripts\\activate      # Windows
```

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 🗄️ Database Setup (MySQL)

### 1️⃣ Create Database

```sql
CREATE DATABASE visitor_db;
```

### 2️⃣ Create Table

```sql
USE visitor_db;

CREATE TABLE visitors (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    phone VARCHAR(15),
    purpose VARCHAR(255),
    date TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

### 3️⃣ Update Database Credentials

Edit **db.py**:

```python
mysql.connector.connect(
    host="localhost",
    user="root",
    password="YOUR_PASSWORD",
    database="visitor_db",
    port=3306
)
```

---

## ▶️ Run the Project

```bash
python app.py
```

Then open your browser:

```
http://127.0.0.1:5000/
```

---

## 🔐 Default Login (if hardcoded)

Check **app.py** for credentials. Example:

```
Username: admin
Password: admin123
```

(Modify for production use)

---


## 🧪 API Routes (Flask)

| Route        | Method   | Description        |
| ------------ | -------- | ------------------ |
| /            | GET      | Show visitors list |
| /login       | GET/POST | Login page         |
| /add         | GET/POST | Add new visitor    |
| /edit/<id>   | GET/POST | Edit visitor       |
| /delete/<id> | GET      | Delete visitor     |

---

## 📝 Notes

* This project is for **learning/demo purposes**.
* Authentication is basic; use Flask-Login or JWT for production.
* Add validation & security before deploying.

---


## ⭐ If you like this project

Give it a ⭐ on GitHub!
