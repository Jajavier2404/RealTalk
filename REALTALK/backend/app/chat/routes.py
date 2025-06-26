from flask import Blueprint, jsonify
from app.models.message import Message

chat_bp = Blueprint('chat', __name__)

@chat_bp.route('/messages', methods=['GET'])
def get_messages():
    messages = Message.query.all()
    return jsonify([msg.to_dict() for msg in messages])
