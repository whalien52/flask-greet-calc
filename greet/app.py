from flask import Flask

app = Flask(__name__)

@app.route('/welcome/')
def welcome():
    return f"Welcome"

@app.route('/welcome/<term>')
def welcome_term(term):
    return f"Welcome {term}"