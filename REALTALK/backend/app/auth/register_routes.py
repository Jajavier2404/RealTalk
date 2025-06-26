from flask import Blueprint, request, jsonify
from .controller import  create_user
from app import db

register_bp = Blueprint('register', __name__)

@register_bp.route('/register', methods=['POST'])
def register():
    data = request.json
    # Validar que los campos necesarios existan
    if not data or 'username' not in data or 'email' not in data or 'password' not in data:
        return jsonify({"msg": "Faltan datos, mi pez. Necesito 'username', 'email' y 'password'."}), 400

    username = data['username']
    email = data['email'] # Sacamos el email del JSON
    password = data['password']

    try:
        # Llamamos a la función create_user con el email
        user = create_user(username, email, password)
        return jsonify({"msg": "Usuario creado, ¡qué bien!", "user_id": user.id}), 201
    except Exception as e:
        # Manejo de errores, por si el email o username ya existen (por ejemplo)
        db.session.rollback() # Si algo falla, revertimos los cambios en la DB
        return jsonify({"msg": f"Hubo un rollo creando el usuario: {str(e)}"}), 500