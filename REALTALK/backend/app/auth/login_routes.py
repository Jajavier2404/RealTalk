from flask import Blueprint, request, jsonify
from flask_jwt_extended import create_access_token
from .controller import verify_user

login_bp = Blueprint('login', __name__)

@login_bp.route('/login', methods=['POST'])
def login():
    data = request.json
    user = verify_user(data['username'], data['password'])
    if not user:
        return jsonify({"msg": "Credenciales incorrectas"}), 401

    token = create_access_token(identity=user.id)
    return jsonify(access_token=token)
