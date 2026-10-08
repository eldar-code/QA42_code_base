import random

from flask import Flask

app = Flask(__name__)


# http://127.0.0.1:5000/api/greet
@app.route("/api/greet", methods=["GET"])
def greet():
    # add some dynamic content to see on page reload
    r = random.randint(1, 10)
    return f"Hello Flask World! - {r}"

# http://127.0.0.1:5000/api/add/40/700
@app.route("/api/add/<int:a>/<int:b>")
def add(a: int, b: int) -> str:
    return str(a + b)


app.run(debug=True)
