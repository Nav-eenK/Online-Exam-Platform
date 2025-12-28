from flask import Flask, render_template,redirect, url_for
import os

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')


@app.route('/login')

def login():
    return render_template('login.html')

@app.route('/register')
def register():
    return render_template('register.html')

port = int(os.environ.get("PORT", 5001))
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=port)