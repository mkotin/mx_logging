from flask import Blueprint, render_template

mod_logs = Blueprint('logs', __name__, url_prefix='/logs')

# Routes
@mod_logs.route('/', methods=['GEt'])
def index():
    return render_template("logs/index.html")
    