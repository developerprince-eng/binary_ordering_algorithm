import os
import numpy as np
from flask import flash, redirect, render_template, url_for, request
from flask_login import current_user, login_user, logout_user, current_user
from werkzeug.security import generate_password_hash
from werkzeug.utils import secure_filename
from . import app, lm
from .models import User
import ime.helpers.boa as BOA

boa = BOA.BOA()

#BAD REQUEST
@app.errorhandler(400)
def resource_error(e):
    return render_template('400.html'), 400

#FORBIDDEN ERROR
@app.errorhandler(403)
def forbidden(e):
    return render_template('403.html'), 403

#NOT ALLOWED ERROR
@app.errorhandler(405)
def method_not_allowed(e):
    return render_template('405.html'), 405

#NOT FOUND ERROR
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

#SERVER INTERNAL ERROR
@app.errorhandler(500)
def server_error(e):
    return render_template('500.html'), 500

#BAD GATEWAY
@app.errorhandler(502)
def server_error_bad_gateway(e):
    return render_template('502.html'), 502

#GATEWAY TIMEOUT
@app.errorhandler(504)
def server_error_gateway_timeout(e):
    return render_template('504.html'), 504

#LOGIN PAGE INDEX
@app.route("/")
def index():
    return render_template("index.html")

#INPUT MACHINE AND PART NUMBER FORM
@app.route("/boa/input1", methods=['GET', 'POST'])
def boaInput():
    if request.method == 'POST':
        return render_template("boa-input.html", machines="0", parts="0")
    return render_template("boa-input.html", machines="0", parts="0")

#INPUT PARTS PRODUCED BY EACH MACHINE
@app.route("/boa/input2", methods=['GET', 'POST'])
def boaInput2():
    if request.method == 'POST':
        machines_number = int(request.form['machines'])
        parts_number = int(request.form['parts'])
        return render_template("boa-input-1.html", machines=machines_number, parts=parts_number)
    return render_template("boa-input-1.html", machines=0, parts=0)

#VIEW THE OUT CELLS FORMATION BY BOA  
@app.route("/boa/input3", methods=['GET', 'POST'])
def boaInput3():
    if request.method == 'POST':
        machines_number = int(request.form['machines'])
        parts_number = int(request.form['parts'])
        buffer_list = [[i for i in range(parts_number)] for j in range(machines_number)]
        buffer_matrix = []
        buffer_temp_list = []
        temp_list = []
        mchnes = range(machines_number)
        prts = range(parts_number)
        for i in mchnes:
            for j in prts:
                temp_list.append(str(i+1) + str(j+1))

        temp_ans_list = []

        for i in temp_list:
            temp_ans_list.append(int(request.form[str(i)]))  

        x=0
        while x<len(temp_ans_list):
            buffer_temp_list.append(temp_ans_list[x:x+parts_number])
            x+=parts_number
        
        buffer_matrix = boa.convert_to_arry(buffer_list)

        while True:
            outputMatrix = boa.order(buffer_matrix)
            if (outputMatrix==buffer_matrix).all()==True:
                break
            else:
                buffer_matrix=outputMatrix
        print(outputMatrix)
        return render_template("boa-output.html", machines=machines_number, parts=parts_number)
    return render_template("boa-output.html")

