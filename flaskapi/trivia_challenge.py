#!/usr/bin/python3
from flask import Flask, redirect, url_for
from flask import request
from flask import render_template
import requests

app = Flask(__name__)

API = "https://opentdb.com/api.php?amount=5&category=24&difficulty=easy&type=multiple"

@app.route("/")
def form_data():
    response = requests.get(f"{API}")
    questions = response.json()
    cards = questions['results'][3]
    print(cards['question'])

@app.route("/correct")
def hello_user(name):
    if name =="correct":
        # return a 302 response to redirect to /correct
        return redirect(url_for("form_data"))
    else:
        
        return redirect(url_for("hello_user"))

if __name__ == "__main__":
   app.run(host="0.0.0.0", port=2224) # runs the application

