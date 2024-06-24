#!/usr/bin/env python3

from flask import Flask
from flask_migrate import Migrate

from models import db

# Create a Flask application instance 
app = Flask(__name__)

# Configure the application
class Config:
    SQLALCHEMY_DATABASE_URI = 'sqlite:///app.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

app.config.from_object(Config)

# Initialize the database and migration tool
db.init_app(app)
migrate = Migrate(app, db)

# Register blueprints here (example)
# from your_blueprint_module import your_blueprint
# app.register_blueprint(your_blueprint)

# Define routes (if not using blueprints)
@app.route('/')
def home():
    return "Welcome to the Flask app!"

if __name__ == '__main__':
    app.run(port=5555, debug=True)

