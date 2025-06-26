from .. import db  # Importación relativa
from ..models.message import Message
from ..models.user import User
from datetime import datetime

class ChatService:
    
    @staticmethod
    def send_message(sender_id, receiver_id, content):
        """Envía un mensaje entre usuarios"""
        try:
            # Verificar que ambos usuarios existan
            sender = User.query.get(sender_id)
            receiver = User.query.get(receiver_id)
            
            if not sender:
                return {'error': 'Usuario emisor no encontrado'}, 404
            if not receiver:
                return {'error': 'Usuario receptor no encontrado'}, 404
            
            # Crear el mensaje
            message = Message(
                sender_id=sender_id,
                receiver_id=receiver_id,
                content=content.strip(),
                timestamp=datetime.utcnow()
            )
            
            db.session.add(message)
            db.session.commit()
            
            return {'message': 'Mensaje enviado exitosamente', 'data': message.to_dict()}, 201
            
        except Exception as e:
            db.session.rollback()
            return {'error': f'Error al enviar mensaje: {str(e)}'}, 500
    
    @staticmethod
    def get_conversation(user1_id, user2_id, limit=50, offset=0):
        """Obtiene la conversación entre dos usuarios"""
        try:
            messages = Message.query.filter(
                ((Message.sender_id == user1_id) & (Message.receiver_id == user2_id)) |
                ((Message.sender_id == user2_id) & (Message.receiver_id == user1_id))
            ).order_by(Message.timestamp.desc())\
             .limit(limit)\
             .offset(offset)\
             .all()
            
            return {
                'messages': [msg.to_dict() for msg in reversed(messages)],
                'count': len(messages)
            }, 200
            
        except Exception as e:
            return {'error': f'Error al obtener conversación: {str(e)}'}, 500
    
    @staticmethod
    def get_user_conversations(user_id):
        """Obtiene todas las conversaciones de un usuario"""
        try:
            # Obtener usuarios únicos con los que se ha intercambiado mensajes
            sent_to = db.session.query(Message.receiver_id.label('user_id'))\
                .filter(Message.sender_id == user_id)\
                .distinct()
            
            received_from = db.session.query(Message.sender_id.label('user_id'))\
                .filter(Message.receiver_id == user_id)\
                .distinct()
            
            # Unir ambas consultas
            all_contacts = sent_to.union(received_from).all()
            
            conversations = []
            for contact in all_contacts:
                other_user_id = contact.user_id
                other_user = User.query.get(other_user_id)
                
                if not other_user:
                    continue
                
                # Obtener el último mensaje
                last_message = Message.query.filter(
                    ((Message.sender_id == user_id) & (Message.receiver_id == other_user_id)) |
                    ((Message.sender_id == other_user_id) & (Message.receiver_id == user_id))
                ).order_by(Message.timestamp.desc()).first()
                
                # Contar mensajes no leídos
                unread_count = Message.query.filter_by(
                    sender_id=other_user_id,
                    receiver_id=user_id,
                    is_read=False
                ).count()
                
                conversations.append({
                    'other_user': other_user.to_dict(),
                    'last_message': last_message.to_dict() if last_message else None,
                    'unread_count': unread_count
                })
            
            # Ordenar por timestamp del último mensaje
            conversations.sort(
                key=lambda x: x['last_message']['timestamp'] if x['last_message'] else '',
                reverse=True
            )
            
            return {'conversations': conversations}, 200
            
        except Exception as e:
            return {'error': f'Error al obtener conversaciones: {str(e)}'}, 500
    
    @staticmethod
    def mark_messages_as_read(user_id, sender_id):
        """Marca los mensajes como leídos"""
        try:
            Message.query.filter_by(
                sender_id=sender_id,
                receiver_id=user_id,
                is_read=False
            ).update({'is_read': True})
            
            db.session.commit()
            return {'message': 'Mensajes marcados como leídos'}, 200
            
        except Exception as e:
            db.session.rollback()
            return {'error': f'Error al marcar mensajes: {str(e)}'}, 500
    
    @staticmethod
    def get_unread_count(user_id, sender_id=None):
        """Obtiene el conteo de mensajes no leídos"""
        query = Message.query.filter_by(receiver_id=user_id, is_read=False)
        
        if sender_id:
            query = query.filter_by(sender_id=sender_id)
        
        return query.count()
