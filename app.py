from flask import Flask, render_template, request, redirect, url_for, session, flash
from werkzeug.security import generate_password_hash, check_password_hash
import mysql.connector
import os

app = Flask(__name__)
app.secret_key = os.environ.get("SECRET_KEY", "fallbacksecret")

# MySQL database connection
def get_db_connection():
    return mysql.connector.connect(
        host=os.environ.get("MYSQL_HOST"),
        user=os.environ.get("MYSQL_USER"),
        password=os.environ.get("MYSQL_PASSWORD"),
        database=os.environ.get("MYSQL_DB")
    )
@app.route("/")
def home():
    if "user" in session:
        return render_template("home.html", user=session["user"])
    return redirect(url_for("login"))

@app.route("/signup", methods=["GET", "POST"])
def signup():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]

        hashed_password = generate_password_hash(password)

        conn = None
        cursor = None

        try:
            conn = get_db_connection()
            cursor = conn.cursor()

            cursor.execute("SELECT * FROM register WHERE username = %s", (username,))
            if cursor.fetchone():
                flash("Username already exists. Try another!", "danger")
                return redirect(url_for("signup"))

            cursor.execute("INSERT INTO register (username, password) VALUES (%s, %s)", (username, hashed_password))
            conn.commit()
            flash("Signup successful! Please log in.", "success")
            return redirect(url_for("login"))

        except Exception as e:
            flash(f"Database error: {e}", "danger")
        finally:
            if cursor:
                cursor.close()
            if conn:
                conn.close()

    return render_template("signup.html")

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]

        conn = None
        cursor = None

        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("SELECT password FROM register WHERE username = %s", (username,))
            result = cursor.fetchone()

            if result and check_password_hash(result[0], password):
                session["user"] = username
                flash("Login successful!", "success")
                return redirect(url_for("home"))
            else:
                flash("Invalid username or password!", "danger")

        except Exception as e:
            flash(f"Database error: {e}", "danger")
        finally:
            if cursor:
                cursor.close()
            if conn:
                conn.close()

    return render_template("login.html")

@app.route("/logout")
def logout():
    session.pop("user", None)
    flash("Logged out successfully!", "info")
    return redirect(url_for("login"))

if __name__ == "__main__":
    app.run(debug=True)
