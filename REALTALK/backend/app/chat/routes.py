from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from .chat_service import ChatService

chat_bp = Blueprint('chat', __name__)

@chat_bp.route('/send', methods=['POST'])
@jwt_required()
def send_message():
    """Endpoint para enviar un mensaje"""
    current_user_id = get_jwt_identity()
    data = request.get_json()
    
    if not data or 'receiver_id' not in data or 'content' not in data:
        return jsonify({'error': 'Datos incompletos'}), 400
    
    if not data['content'].strip():
        return jsonify({'error': 'El mensaje no puede estar vacío'}), 400
    
    result, status_code = ChatService.send_message(
        sender_id=current_user_id,
        receiver_id=data['receiver_id'],
        content=data['content']
    )
    
    return jsonify(result), status_code

@chat_bp.route('/conversation/<int:user_id>', methods=['GET'])
@jwt_required()
def get_conversation(user_id):
    """Endpoint para obtener conversación con un usuario específico"""
    current_user_id = get_jwt_identity()
    
    limit = request.args.get('limit', 50, type=int)
    offset = request.args.get('offset', 0, type=int)
    
    result, status_code = ChatService.get_conversation(
        user1_id=current_user_id,
        user2_id=user_id,
        limit=limit,
        offset=offset
    )
    
    return jsonify(result), status_code

@chat_bp.route('/conversations', methods=['GET'])
@jwt_required()
def get_conversations():
    """Endpoint para obtener todas las conversaciones del usuario"""
    current_user_id = get_jwt_identity()
    
    result, status_code = ChatService.get_user_conversations(current_user_id)
    return jsonify(result), status_code

@chat_bp.route('/mark-read/<int:sender_id>', methods=['PUT'])
@jwt_required()
def mark_as_read(sender_id):
    """Endpoint para marcar mensajes como leídos"""
    current_user_id = get_jwt_identity()
    
    result, status_code = ChatService.mark_messages_as_read(
        user_id=current_user_id,
        sender_id=sender_id
    )
    
    return jsonify(result), status_code

@chat_bp.route('/unread-count', methods=['GET'])
@jwt_required()
def get_unread_count():
    """Endpoint para obtener el conteo de mensajes no leídos"""
    current_user_id = get_jwt_identity()
    sender_id = request.args.get('sender_id', type=int)
    
    count = ChatService.get_unread_count(current_user_id, sender_id)
    return jsonify({'unread_count': count}), 200
