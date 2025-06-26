from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from flask_jwt_extended import JWTManager
from flask_socketio import SocketIO
from .config import Config

db = SQLAlchemy()
jwt = JWTManager()
socketio = SocketIO(cors_allowed_origins="*")

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    jwt.init_app(app)
    CORS(app)
    socketio.init_app(app)

    # Importar y registrar rutas
    from .auth.login_routes import login_bp
    from .auth.register_routes import register_bp
    from .chat.routes import chat_bp

    app.register_blueprint(login_bp, url_prefix='/auth')
    app.register_blueprint(register_bp, url_prefix='/auth')
    app.register_blueprint(chat_bp, url_prefix='/chat')

    return app
