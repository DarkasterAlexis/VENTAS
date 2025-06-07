from flask import Flask, request,render_template,redirect,url_for
from controllers import usuario_controller, cliente_controller, producto_controller, venta_controller
from flask_login import LoginManager,login_required, logout_user, login_user,UserMixin,current_user
from database import db

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///ventas.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db.init_app(app)
app.secret_key = 'Darkaster_7024'
login_manager = LoginManager()
login_manager.login_view = 'usuario.login'
login_manager.init_app(app)

app.register_blueprint(usuario_controller.usuario_bp)
app.register_blueprint(cliente_controller.cliente_bp)
app.register_blueprint(producto_controller.producto_bp)
app.register_blueprint(venta_controller.venta_bp)

from models.usuario_model import Usuario


@app.context_processor
def inject_active_path():
    def is_active(path):
        return 'active' if request.path == path else ''
    return (dict(is_active = is_active))

@login_manager.user_loader
def load_user(user_id):
    return Usuario.get_by_id(user_id)

@app.route('/')
def home():
    return render_template('index.html') 

if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True)