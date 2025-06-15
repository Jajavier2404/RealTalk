from flask import Flask
from flask_cors import CORS
from flask_socketio import SocketIO
from .config import Config
from db.database import Base, engine
from app.models import user, message, session  

socketio = SocketIO(cors_allowed_origins="*")

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    CORS(app)
    socketio.init_app(app)

    # Crear las tablas en la base de datos
    Base.metadata.create_all(bind=engine)

    # Registrar rutas (ejemplo)
    # from app.auth.login_routes import auth_bp
    # app.register_blueprint(auth_bp, url_prefix="/auth")

    @app.route('/')
    def index():
        return {"mensaje": "Hola desde Flask y base de datos 😎"}

    return app
