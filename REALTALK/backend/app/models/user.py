from .. import db  # Importación relativa
from sqlalchemy.orm import relationship

class User(db.Model):
    __tablename__ = 'users'
    
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(200), nullable=False)
    email = db.Column(db.String(120), unique=True, index=True, nullable=False)
    
    # Relaciones para mensajes
    sent_messages = relationship('Message', foreign_keys='Message.sender_id', backref='sender', lazy='dynamic')
    received_messages = relationship('Message', foreign_keys='Message.receiver_id', backref='receiver', lazy='dynamic')
    
    def to_dict(self):
        return {
            'id': self.id,
            'username': self.username,
            'email': self.email
        }