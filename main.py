from flask import Flask
from flask import render_template

import random

app = Flask(__name__)


@app.route('/')
def index():
    return '<h1>Hello from Flask!<h1>'
           

@app.route('/about')
def about():
      return render_template("about.html")   


@app.route('/lucky')
def lucky ():
  number = random.randrange(120)
  return render_template("lucky.html", num=number)
