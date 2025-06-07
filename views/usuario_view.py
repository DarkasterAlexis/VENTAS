from flask import render_template

def list(usuarios):
    return render_template('usuarios/index.html',usuarios= usuarios)

def create():
    return render_template('usuarios/create.html')

def edit(usuarios):
    return render_template('usuarios/edit.html',usuarios= usuarios)

def login():
    return render_template("login.html")

def dashboard(usuario):
    return render_template("dashboard.html",usuario=usuario)

def register():
    return render_template("register.html")