from flask import Flask, render_template, redirect, url_for, request, flash
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user, logout_user, login_required, current_user
from extensions import db, login_manager
from models import User, Todo
import os

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///todo.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)
login_manager.init_app(app)

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


# ---------- AUTH ROUTES ----------
@app.route('/register', methods=["GET", "POST"])
def register():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")

        if User.query.filter_by(username=username).first():
            flash("Username already exists!", "danger")
            return redirect(url_for("register"))

        new_user = User(
            username=username,
            password=generate_password_hash(password)
        )
        db.session.add(new_user)
        db.session.commit()

        flash("Account created successfully!", "success")
        return redirect(url_for("login"))

    return render_template("register.html")


@app.route('/login', methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")

        user = User.query.filter_by(username=username).first()

        if user and check_password_hash(user.password, password):
            login_user(user)
            return redirect(url_for("dashboard"))
        else:
            flash("Invalid username or password!", "danger")

    return render_template("login.html")


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for("login"))


# ---------- TODO ROUTES ----------
@app.route('/')
@login_required
def dashboard():
    tasks = Todo.query.filter_by(user_id=current_user.id).all()
    return render_template("dashboard.html", tasks=tasks)


@app.route('/add', methods=["POST"])
@login_required
def add():
    task = request.form.get("task")

    if task.strip():
        new_task = Todo(task=task, user_id=current_user.id)
        db.session.add(new_task)
        db.session.commit()

    return redirect(url_for("dashboard"))


@app.route('/delete/<int:id>')
@login_required
def delete(id):
    task = Todo.query.get(id)
    if task and task.user_id == current_user.id:
        db.session.delete(task)
        db.session.commit()
    return redirect(url_for("dashboard"))


# ---------- CREATE DB ----------
with app.app_context():
    if not os.path.exists("instance"):
        os.makedirs("instance")
    db.create_all()


if __name__ == "__main__":
    app.run(debug=True)
