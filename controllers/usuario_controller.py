from flask import request,redirect,url_for,Blueprint, flash
from models.usuario_model import Usuario
from views import usuario_view
from flask_login import login_user, login_required,logout_user,current_user
from werkzeug.security import check_password_hash

usuario_bp = Blueprint('usuario',__name__,url_prefix="/usuarios")

@usuario_bp.route("/")
def index():
    usuarios = Usuario.get_all()
    return usuario_view.list(usuarios)

@usuario_bp.route("/create",methods=['GET','POST'])
def create():
    if request.method == 'POST':
        nombre = request.form['nombre']
        username = request.form['username']
        password = request.form['password']
        rol = request.form['rol']
        usuario = Usuario(nombre,username,password,rol)
        usuario.save()
        return redirect(url_for('usuario.index'))
    return usuario_view.create()

@usuario_bp.route("/edit/<int:id>",methods=['GET','POST'])
def edit(id):
    usuario = Usuario.get_by_id(id)
    if request.method == 'POST':
        nombre = request.form['nombre']
        username = request.form['username']
        password = request.form['password']
        rol = request.form['rol']
        usuario.update(nombre=nombre,username=username,password=password,rol=rol)
        return redirect(url_for('usuario.index'))
    return usuario_view.edit(usuario)

@usuario_bp.route("/delete/<int:id>",methods=['GET','POST'])
def delete(id):
    usuario = Usuario.get_by_id(id)
    usuario.delete()
    return redirect(url_for('usuario.index'))

@usuario_bp.route("/login",methods=['GET','POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user = Usuario.get_by_username(username)
        if user and check_password_hash(user.password, password):
            login_user(user)
            flash('INICIO DE SESION EXITOSO','success')
            return redirect(url_for("usuario.dashboard"))
        else:
            flash('Credenciales Invalidas','danger')
    return usuario_view.login()

@usuario_bp.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for("usuario.login"))

@usuario_bp.route("/dashboard")
@login_required
def dashboard():
    return usuario_view.dashboard(current_user)

@usuario_bp.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        nombre = request.form['nombre']
        username = request.form['username']
        password = request.form['password']
        rol = 'cliente'  # o un rol predeterminado si no lo elige el usuario
        nuevo_usuario = Usuario(nombre, username, password, rol)
        nuevo_usuario.save()
        return redirect(url_for('usuario.login'))
    return usuario_view.register()
