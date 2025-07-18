from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for, current_app
)

import json

from werkzeug.exceptions import abort

bp = Blueprint('data', __name__)

@bp.route('/data')
def data():

    with open(current_app.root_path + "/data/data") as file:
        data = json.load(file)
    
    return render_template('data.html', var=data)