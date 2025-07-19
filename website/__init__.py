import os
from flask import Flask, current_app, g
from flask_pymongo import PyMongo


def create_app():

    # create instance of application
    app = Flask(__name__, instance_relative_config=True)

    # init config variables
    app.config.from_prefixed_env()

    # create instance folder if necessary
    try:
        os.mkdir(app.instance_path)
    except OSError:
        pass

    from . import data
    app.register_blueprint(data.bp)
    
    return app