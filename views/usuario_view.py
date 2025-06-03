from flask import render_template

def list(usuario):
    return render_template('usuario/index.html',usuario= usuario)

def create():
    return render_template('usuario/create.html')

def edit(usuario):
    return render_template('usuario/edit.html',usuario= usuario)