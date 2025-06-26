from app.models.user import User
from app import db
from werkzeug.security import generate_password_hash, check_password_hash

def create_user(username, password):
    hashed_password = generate_password_hash(password)
    user = User(username=username, password=hashed_password)
    db.session.add(user)
    db.session.commit()
    return user

def verify_user(username, password):
    user = User.query.filter_by(username=username).first()
    if user and check_password_hash(user.password, password):
        return user
    return None
