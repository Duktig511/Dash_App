from flask import Flask
from flask_nav import Nav
from flask_bootstrap import  Bootstrap

app = Flask(__name__)
from dashApp import routes


nav = Nav(app)
Bootstrap(app)