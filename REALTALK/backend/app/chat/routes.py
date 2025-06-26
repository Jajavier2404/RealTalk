# app/chat/routes.py
from flask import Blueprint, request, jsonify
# Suponiendo que necesitas 'db' para operaciones de base de datos y 'socketio' para tiempo real
from app import db, socketio # <--- CAMBIA ESTA LÍNEA

chat_bp = Blueprint('chat', __name__)

# Ejemplo de ruta que podría usar db o socketio
@chat_bp.route('/send_message', methods=['POST'])
def send_message():
    data = request.json
    sender_id = data.get('sender_id')
    content = data.get('content')

    if not sender_id or not content:
        return jsonify({"error": "Sender ID and content are required"}), 400

    try:
        new_message = Message(sender_id=sender_id, content=content)
        db.session.add(new_message)
        db.session.commit()

        # Emitir el mensaje a todos los clientes conectados
        socketio.emit('new_message', new_message.to_dict())

        return jsonify({"message": "Message sent successfully!"}), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 500

# Recuerda importar tu modelo Message si lo estás usando aquí
from app.models.message import Message # Asumiendo que Message está en app/models/message.py o similar