"""Flask app for Cupcakes"""

from flask import Flask, request, jsonify, render_template

#TODO: rename
from models import db, connect_db, Cupcake, DEFAULT_IMAGE

app = Flask(__name__)

#TODO: rename
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///______'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = "oh-so-secret"
app.config['SQLALCHEMY_ECHO'] = True

connect_db(app)