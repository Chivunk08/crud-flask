import os
from flask import Flask, render_template
from flask_migrate import Migrate
from models.user import db

app = Flask(__name__)

app.config.from_object('config')

db.init_app(app)

migrate = Migrate(app,db)

@app.route("/",methods=['GET'])
def homepage():
    return render_template("homepage.html")





