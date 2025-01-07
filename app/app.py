from flask import Flask, jsonify
import socket, requests, time, os
from dotenv import load_dotenv

app = Flask(__name__)
load_dotenv()

def json_response(data):
    response = {
        "_version": "VERSION 2",
        "_host": socket.gethostname(),
        "_time": time.time(),
        "_data": data
    }
    return jsonify(response)

@app.route("/")
@app.route("/index")
def index():
    data = {"message": "Happy new year 2025"}
    return json_response(data)

@app.route('/ping')
def ping():

    return json_response('pong')

@app.route('/news', defaults={'country_name': 'US'})
@app.route('/news/<country_name>')
def news(country_name):
    api_key = os.getenv('NEWSAPI_DOT_ORG_API_KEY')
    base_url = "http://newsapi.org/v2/top-headlines?"
    complete_url = base_url + "country=" + country_name + "&apiKey=" + api_key
    data = requests.get(complete_url)
    return json_response(data.json())

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=8000)