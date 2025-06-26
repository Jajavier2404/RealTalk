from flask import Blueprint, request, jsonify
from app import db  # <- Importación corregida
from app.models.message import Message  # <- Asegúrate que esta importación también sea correcta

chat_bp = Blueprint("chat", __name__)

@chat_bp.route("/chat/messages", methods=["POST"])
def create_message():
    data = request.json
    user_id = data.get("user_id")
    content = data.get("content")

    if not user_id or not content:
        return jsonify({"error": "Faltan datos"}), 400

    session = db()  # <-- Crear sesión
    try:
        message = Message(user_id=user_id, content=content)
        session.add(message)
        session.commit()
        session.refresh(message)
        return jsonify({"id": message.id, "user_id": message.user_id, "content": message.content}), 201
    except Exception as e:
        session.rollback()
        return jsonify({"error": str(e)}), 500
    finally:
        session.close()  # <-- Cerrar sesión
