from flask import Flask, render_template, request, redirect, url_for
import sqlite3
from password_handling import encryptPassword

app = Flask(__name__)

# Your 'encryptPassword()' function here

# Route to handle login requests
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        # Hash the provided password
        hashed_password = encryptPassword(password)

        # Check the database for the username and hashed password
        conn = sqlite3.connect('users.db')
        cursor = conn.cursor()
        cursor.execute("SELECT hashed_password FROM users_table WHERE username = ?", (username,))
        result = cursor.fetchone()
        conn.close()

        if result is not None and result[0] == hashed_password:
            # Login successful, redirect to index.html
            return redirect(url_for('index'))
        else:
            error = "Invalid username or password. Please try again."
            return render_template('login.html', error=error)

    # If it's a GET request or no login credentials provided, show the login page.
    return render_template('login.html')

# Route to handle registration requests
@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        # Hash the provided password
        hashed_password = encryptPassword(password)

        # Insert the username and hashed password into the database
        conn = sqlite3.connect('users.db')
        cursor = conn.cursor()
        cursor.execute("INSERT INTO users_table (username, hashed_password) VALUES (?, ?)", (username, hashed_password))
        conn.commit()
        conn.close()

        # Registration successful, redirect to login page
        return redirect(url_for('login'))

    # If it's a GET request or no registration credentials provided, show the registration page.
    return render_template('registration.html')

# Route for the index.html page after successful login
@app.route('/index')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run()
