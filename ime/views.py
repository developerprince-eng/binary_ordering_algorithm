import os
import numpy as np
from flask import flash, redirect, render_template, url_for, request
from flask_login import current_user, login_user, logout_user, current_user
from werkzeug.security import generate_password_hash
from werkzeug.utils import secure_filename
from . import app, lm
from .models import User
# import helpers.boa as BOA

# boa = BOA.BOA()

@app.errorhandler(403)
def forbidden(e):
    return render_template('403.html'), 403


@app.errorhandler(405)
def method_not_allowed(e):
    return render_template('405.html'), 405


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


@app.errorhandler(500)
def server_error(e):
    return render_template('500.html'), 500

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/boa/input", methods=['GET', 'POST'])
def boaInput():
    if "step" not in request.form:
        return render_template("boa-input.html", step="step-1")
    elif request.form["step"] == "step-2":
        return render_template("boa-input.html", step="step-2")
    elif request.form["step"] == "step-3":
        return render_template("boa-input.html", step="step-3")

