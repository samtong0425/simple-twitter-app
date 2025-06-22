import sqlite3
import os
from flask import Flask, session, render_template, redirect, flash, request
from flask_session import Session
from functools import wraps
from werkzeug.security import generate_password_hash, check_password_hash


app = Flask(__name__)

app.config["SECRET_KEY"] = os.urandom(24)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_USE_SIGNER"] = True
app.config["SESSION_TYPE"] = "filesystem"

DATABASE_NAME = "main.db"

# --- DATABASE FUNCTIONS (MOVE THESE UP!) ---
def get_db_connection():
    """Returns a database connection."""
    conn = sqlite3.connect(DATABASE_NAME)
    conn.row_factory = sqlite3.Row
    return conn

def init_db():
    conn = get_db_connection()
    conn.execute(
        """
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT NOT NULL UNIQUE,
            hashed_password TEXT NOT NULL,
            registered_at DATETIME DEFAULT CURRENT_TIMESTAMP
        )
        """
    )

    conn.execute(
        """
        CREATE TABLE IF NOT EXISTS posts (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER NOT NULL,
            title TEXT NOT NULL,
            content TEXT NOT NULL,
            timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY (user_id) REFERENCES users (id)
        )
        """
    )

    conn.commit()
    conn.close()
# --- END DATABASE FUNCTIONS ---


# --- CALL init_db() AFTER ITS DEFINITION ---
with app.app_context():
    init_db()
# --- END CALL init_db() ---


Session(app) # Initialize Flask-Session AFTER the app context and db init


def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if session.get("user_id") is None:
            return redirect("/login")
        return f(*args, **kwargs)

    return decorated_function


@app.after_request
def after_request(response):
    """Ensure responses aren't cached"""
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response


@app.route("/")
def index():
    """Home Feed - Show all posts sorted by time"""
    conn = get_db_connection()
    posts = conn.execute(
        """
        SELECT
            posts.id,
            posts.title,
            posts.content,
            posts.timestamp,
            users.username
        FROM posts
        JOIN users ON posts.user_id = users.id
        ORDER BY posts.timestamp DESC
        """
    ).fetchall()
    conn.close()

    return render_template("homepage.html", posts=posts)


@app.route("/register", methods=["GET", "POST"])
def register():
    """Register user"""
    if request.method == "GET":
        return render_template("register.html")

    elif request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        confirmation = request.form["confirmation"]

        if not username:
            flash("Username cannot be empty.")
            return redirect("/register")
        if not password:
            flash("Password cannot be empty.")
            return redirect("/register")
        if not confirmation:
            flash("Password confirmation cannot be empty.")
            return redirect("/register")
        if password != confirmation:
            flash("Passwords do not match.")
            return redirect("/register")

        conn = get_db_connection()
        cursor = conn.execute("SELECT * FROM users WHERE username = ?", (username,))
        row = cursor.fetchone()
        if row is not None:
            flash("Username has been taken")
            conn.close()
            return redirect("/register")

        hashed_password = generate_password_hash(password)
        cursor = conn.execute(
            "INSERT INTO users (username, hashed_password) VALUES (?, ?)",
            (username, hashed_password),
        )
        conn.commit()
        new_id = cursor.lastrowid
        conn.close()

        session["user_id"] = new_id
        flash(f"Welcome, {username}!")
        return redirect("/")


@app.route("/login", methods=["GET", "POST"])
def login():
    """Log user in"""
    session.clear()

    if request.method == "GET":
        return render_template("login.html")
    elif request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")

        if not username or not password:
            flash("Must provide username and password")
            return render_template("login.html")

        conn = get_db_connection()
        cursor = conn.execute("SELECT * FROM users WHERE username = ?", (username,))
        user = cursor.fetchone()
        conn.close()

        if user is None or not check_password_hash(user["hashed_password"], password):
            flash("Invalid username or password")
            return render_template("login.html")

        session["user_id"] = user["id"]
        flash(f"Welcome back, {username}!")
        return redirect("/")


@app.route("/logout")
def logout():
    """Log user out"""
    session.clear()
    flash("You have been logged out.")
    return redirect("/")


@app.route("/create", methods=["GET", "POST"])
@login_required
def create_post():
    """Create a new post"""
    if request.method == "GET":
        return render_template("create_post.html")
    elif request.method == "POST":
        title = request.form.get("title")
        content = request.form.get("content")

        MAX_TITLE_CHARS = 100
        MAX_CONTENT_CHARS = 1000
        MAX_CONTENT_WORDS = 150

        if not title:
            flash("Post title cannot be empty.")
            return redirect("/create")
        if len(title) > MAX_TITLE_CHARS:
            flash(f"Post title exceeds {MAX_TITLE_CHARS} characters.")
            return redirect("/create")

        if not content:
            flash("Post content cannot be empty.")
            return redirect("/create")
        if len(content) > MAX_CONTENT_CHARS:
            flash(f"Post content exceeds {MAX_CONTENT_CHARS} characters.")
            return redirect("/create")

        content_words = content.strip().split() if content.strip() else []
        if len(content_words) > MAX_CONTENT_WORDS:
            flash(f"Post content exceeds {MAX_CONTENT_WORDS} words.")
            return redirect("/create")

        user_id = session["user_id"]
        conn = get_db_connection()
        conn.execute(
            "INSERT INTO posts (user_id, title, content) VALUES (?, ?, ?)",
            (user_id, title, content)
        )
        conn.commit()
        conn.close()
        flash("Post created successfully!")
        return redirect("/")