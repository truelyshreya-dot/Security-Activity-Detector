import os
from flask import Flask, render_template, request
from scanner import scan

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def home():
    result = ""

    if request.method == "POST":
        text = request.form.get("text", "")
        result = scan(text)

    return render_template("index.html", result=result)


if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=int(os.environ.get("PORT", 5000)),
        debug=True
    )