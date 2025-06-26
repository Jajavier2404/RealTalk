from app import db
from datetime import datetime

class Session(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, nullable=False)
    token = db.Column(db.String(500), nullable=False)
    ip_address = db.Column(db.String(100))
    device_info = db.Column(db.String(200))
    login_time = db.Column(db.DateTime, default=datetime.utcnow)
    is_active = db.Column(db.Boolean, default=True)

    def to_dict(self):
        return {
            "id": self.id,
            "user_id": self.user_id,
            "token": self.token,
            "ip_address": self.ip_address,
            "device_info": self.device_info,
            "login_time": self.login_time.isoformat(),
            "is_active": self.is_active
        }
