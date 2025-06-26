from app import db
from app.models.message import Message

def save_message(sender_id, content):
    message = Message(sender_id=sender_id, content=content)
    db.session.add(message)
    db.session.commit()
    return message
