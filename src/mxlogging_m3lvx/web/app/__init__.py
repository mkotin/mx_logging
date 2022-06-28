from flask import Flask, redirect, render_template, url_for
from mxlogging_m3lvx.web.app.logs.controllers import mod_logs as log_module
from flask.logging import default_handler

# from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
# app.config.from_object('config')
app.debug = False
app.use_reloader=False
app.logger.removeHandler(default_handler)
app.logger.disabled = True





# db = SQLAlchemy(app)

# Sample HTTP error handling
@app.errorhandler(404)
def not_found(error):
    return render_template('404.html'), 404

# Registering blueprints
app.register_blueprint(log_module)

@app.route('/')
def home():
    return redirect(url_for('logs.index'))
