from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for, current_app
)



import json
from flask_pymongo import PyMongo

from werkzeug.exceptions import abort

bp = Blueprint('data', __name__)

@bp.route('/data')
def data():

    host = current_app.config['MONGO_HOST']
    database = current_app.config['MONGO_DATABASE']

    app = current_app._get_current_object()
    mongo = PyMongo(app, uri=f"{host}{database}")

    tickets = mongo.db.tickets.find().sort("created_at", -1)

    return render_template('data.html', tickets=tickets)