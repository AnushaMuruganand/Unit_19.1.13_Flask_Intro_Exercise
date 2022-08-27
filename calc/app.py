# Put your app in here.

from flask import Flask, request
from operations import add, sub, mult, div

app = Flask(__name__)

@app.route('/add')
def addition():
    """ Add a and b parameters """

    a = int(request.args["a"])
    b = int(request.args["b"])

    addition = add(a,b)

    return f"<h1>Addition of {a} and {b} : {addition}<h1>"

@app.route('/sub')
def subtract():
    """ Subtract a and b parameters """

    a = int(request.args["a"])
    b = int(request.args["b"])

    subtract = sub(a,b)

    return f"<h1>Subtraction of {a} and {b} : {subtract}<h1>"

@app.route('/mult')
def mutiply():
    """ Mutiply a and b parameters """

    a = int(request.args["a"])
    b = int(request.args["b"])

    mutiply = mult(a,b)

    return f"<h1>Multiplication of {a} and {b} : {mutiply}<h1>"

@app.route('/div')
def division():
    """ Dividing a and b parameters """

    a = int(request.args["a"])
    b = int(request.args["b"])

    division = div(a,b)

    return f"<h1>Division of {a} and {b} : {division}<h1>"  

# Further Study

operations = {
    'add': add,
    'sub': sub,
    'div': div,
    'mult': mult,
}

@app.route('/math/<operator>')
def math_operations(operator):
    operation = operations[operator]

    a = int(request.args["a"])
    b = int(request.args["b"])

    result = operation(a,b)

    return f" <h1> {operator.capitalize()} of {a} and {b} : {result}"

