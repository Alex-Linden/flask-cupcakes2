"""Flask app for Cupcakes"""

from flask import Flask, request, jsonify, render_template

#TODO: rename
from models import db, connect_db, Cupcake, DEFAULT_IMAGE

app = Flask(__name__)

#TODO: rename
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cupcakes2'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = "oh-so-secret"
app.config['SQLALCHEMY_ECHO'] = True

connect_db(app)

@app.get("/")
def root():
    """Render homepage."""

    return render_template("index.html")

@app.get("/api/cupcakes")
def list_cupcakes()
    """Return info on all cupcakes like
    {cupcakes: [{id, flavor, size, rating, image}, ...]}"""

    cupcakes = [cupcake.serialize() for cupcake in Cupcake.query.all()]
    return jsonify(cupcakes=cupcakes)

