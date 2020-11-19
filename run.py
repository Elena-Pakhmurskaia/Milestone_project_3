import os
import json
from flask import Flask, render_template


app = Flask(__name__)


@app.route("/")
def index():
    data = []
    with open("data/birds.json", "r") as json_data:
        data = json.load(json_data)

    return render_template("index.html", page_title="Home", birds=data)


@app.route('/index/<bird_name>')
def about_bird(bird_name):
    bird = {}

    with open("data/birds.json", "r") as json_data:
        data = json.load(json_data)
        for obj in data: 
            if obj["url"] == bird_name:
                bird = obj

    return render_template("endangered_birds.html", endangered_bird=bird)


@app.route("/hot_locations")
def hot_locations():
    
    return render_template("hot_locations.html")


if __name__ == "__main__":
    app.run(
        host=os.environ.get("IP", "0.0.0.0"),
        port=int(os.environ.get("PORT", "5000")),
        debug=True)
    