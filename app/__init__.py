#__init__.py initializes the app package to be used in main.py
#this script will setup the flask app and database, register the blueprints, and configure the app / database

#imports
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

#initialize the database
db = SQLAlchemy()

#function to create the app and return it
def createApp():
    #create the app
    app = Flask(__name__)
    #configure the app
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False #disable modification tracking for performance inhancement

    #initialize the database
    db.init_app(app)

    #register the routes blueprint
    from .routes import view
    app.register_blueprint(view)

    #create the database using a context manager
    with app.app_context():
        #make sure the correct model is being imported
        from .models import Transaction
        #create the database
        db.create_all()

    #return the app
    return app

