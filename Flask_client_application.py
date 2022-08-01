from flask import *
import requests
import json

app = Flask(__name__)

@app.route("/")
def inicio():
    return render_template("index.html")


if __name__ == "__main__":
    app.run(port = 4000)