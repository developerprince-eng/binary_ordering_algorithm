import os
import numpy as np
from flask import flash, redirect, render_template, url_for, request
from flask_login import current_user, login_user, logout_user, current_user
from werkzeug.security import generate_password_hash
from werkzeug.utils import secure_filename
from . import app, lm
from .models import User

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
    def order(a):

        row = a.shape[0]
        col = a.shape[1]
        lst = []

        for i in a[1:]:
            sum1 = 0
            k = 3
            for item in i[1:-1]:
                item = int(item)
                sum1 = int(sum1 + item * (2 ** (col - k)))
                k = k + 1
                i[-1] = sum1
                lst.append(int(sum1))

        lst1 = sorted(lst,reverse=True)

        if lst == lst1:
            pass
        else:
            a = a[np.argsort(a[:, -1].astype(int))[::-1]]

        lst = []
        for i in a[1:]:
            i[-1] = 0
        a = a.T


        for i in a[1:-1]:
            sum1 = 0
            k=2
            for item in i[1:]:

                item = int(item)
                sum1 = int(sum1 + item * (2 ** (row - k)))
                k = k + 1
                i[-1] = sum1
                lst.append(int(sum1))
        lst1 = sorted(lst,reverse=True)

        if lst == lst1:
            pass
        else:
            a = a[np.argsort(a[:, -1].astype(int))[::-1]]
        for i in a[1:]:
            i[-1]=0
        a = a.T
        return a
    matrix = np.array([("Ma","p1","p2","p3","p4","p5","p6","p7","1000"),("A",1,1,0,0,1,0,0,0),("B",0,0,1,0,0,0,0,1),("C",0,1,1,0,0,1,1,0),("D",0,0,0,1,0,0,0,1),("E",0,0,1,1,0,1,1,0),("F",1,1,0,0,1,0,0,0),(1000,0,0,0,0,0,0,0,100)])

    while True:
        buffer = order(matrix)
        if (buffer==matrix).all()==True:
            break
        else:
            matrix=buffer
    print(buffer)

    return render_template("index.html")