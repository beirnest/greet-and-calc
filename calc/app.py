from flask import Flask, request
from operations import add, sub, mult, div

app = Flask(__name__)

@app.route("/add")
def add_request():
    """Handles addition requests"""

    a = request.args.get("a")
    b = request.args.get("b")
    total = add(int(a), int(b))
    return f"{total}"

@app.route("/sub")
def sub_request():
    """Handles subtraction requests"""

    a = request.args.get("a")
    b = request.args.get("b")
    total = sub(int(a), int(b))
    return f"{total}"

@app.route("/mult")
def mult_request():
    """Handles multiplication requests"""

    a = request.args.get("a")
    b = request.args.get("b")
    total = mult(int(a), int(b))
    return f"{total}"

@app.route("/div")
def div_request():
    """Handles division requests"""

    a = request.args.get("a")
    b = request.args.get("b")
    total = div(int(a), int(b))
    return f"{total}"