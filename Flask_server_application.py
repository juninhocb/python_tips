from flask import *
import requests
import json
app = Flask(__name__)

@app.route("/welcome", methods = ['POST', 'GET'])
def index():
    body = request.get_json(force = True)
    print("Mensagem recebida " + str(body))
    response  =  'Simple application with Flask!' if body == "welcome" else "Dont recognize it"
    return json.dumps(response)

if __name__ == "__main__":
    app.run(host = "0.0.0.0", port = 4001)