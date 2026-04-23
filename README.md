# 📝 Flask To-Do List Application

A simple and efficient To-Do List web application built using Flask.
This project allows users to manage daily tasks with features like adding, updating, and deleting tasks.

---

## 🚀 Features

* ➕ Add new tasks
* 📝 Update existing tasks
* ❌ Delete tasks
* ✔️ Mark tasks as completed
* 📅 Task tracking system
* 🌐 Clean and simple UI

---

## 🛠️ Tech Stack

* **Backend:** Flask (Python)
* **Database:** SQLite (via SQLAlchemy)
* **Frontend:** HTML, CSS (Jinja Templates)
* **ORM:** SQLAlchemy

---

## 📂 Project Structure

```
project-folder/
│
├── instance/              # Instance-specific files (database)
├── static/                # CSS, JS, images
├── templates/             # HTML templates
│
├── app.py                 # Main Flask application
├── models.py              # Database models
├── extensions.py          # App extensions (DB, etc.)
├── requirements.txt       # Dependencies
├── Procfile               # Deployment file (for Heroku/Render)
│
├── __pycache__/           # Python cache files
```

---

## ⚙️ Installation & Setup

### 1. Clone the Repository

```bash
git clone https://github.com/rajeshgowda116/your-repo-name.git
cd your-repo-name
```

---

### 2. Create Virtual Environment

```bash
python -m venv venv
venv\Scripts\activate      # Windows
source venv/bin/activate   # Linux / Mac
```

---

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

### 4. Run the Application

```bash
python app.py
```

---

### 5. Open in Browser

```
http://127.0.0.1:5000/
```

---

## 📌 Example Model

```python
class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200))
    completed = db.Column(db.Boolean, default=False)
```

---

## 🌍 Deployment

This project includes a `Procfile`, so it can be deployed on:

* Heroku
* Render
* Railway

---

## 🌟 Future Enhancements

* 🔐 User authentication system
* ⏰ Task reminders
* 📱 Responsive UI (Bootstrap)
* 📊 Dashboard with analytics
* 🌐 REST API integration

---

## 🤝 Contributing

Feel free to fork and improve this project!

---

## 👨‍💻 Author

**Rajesh Gowda**
GitHub: https://github.com/rajeshgowda116
