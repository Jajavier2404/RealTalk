from flask import Blueprint, request, jsonify
from .controller import create_user

register_bp = Blueprint('register', __name__)

@register_bp.route('/register', methods=['POST'])
def register():
    data = request.json
    user = create_user(data['username'], data['password'])
    return jsonify({"msg": "Usuario creado", "user_id": user.id}), 201
