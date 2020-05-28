from flask import Flask, request
from operations import add, sub, mult, div

app = Flask(__name__)

@app.route('/calc')
def calc():
    return 'hi'

@app.route('/calc/<term>')
def calculate(term):
    num1 = request.args['a']
    num2 = request.args['b']
    valid = {"add" : '+', "sub" : '-', "mult": '*', 'div': '/'}

    if term in valid:
        output = eval(num1 + valid[term] + num2)
        return f"{output}"
    else:
        return 'There was an error with your operation'