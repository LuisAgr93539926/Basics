from flask import Flask, request
from random import randint, choice
from datetime import datetime

app = Flask(__name__)

"""
    This api is also hosted publicly, to access use this url: https://tokog44785.pythonanywhere.com/ 
"""

@app.route("/")
def index():
    phrases: list[str] = ["Welcome!", "You are looking good today", "How are you!"]
    return {"phrase": choice(phrases), "date": datetime.now()}


@app.route("/api/random/")
def random():
    number_input: int = request.args.get("number", type=int)
    text_input: str = request.args.get("text", type=str, default="Hello World!")

    if isinstance(number_input, int):
        return {
            "input": number_input,
            "text": text_input,
            "random": randint(0, number_input),
            "date": datetime.now(),
        }
    else:
        return {"Error": "Please only enter numbers (e.g. ?number=10)"}


if __name__ == "__main__":
    app.run()
