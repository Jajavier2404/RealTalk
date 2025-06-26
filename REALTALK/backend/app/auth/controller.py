from app.models.user import User
from app import db
from werkzeug.security import generate_password_hash, check_password_hash
from sqlalchemy.exc import IntegrityError # Importamos este error específico

def create_user(username, email, password):
    """
    Crea un nuevo usuario, verificando antes si el username o email ya existen.
    Retorna el objeto User si es exitoso, o None si hay una violación de unicidad.
    """
    # Primero, verificamos si ya existe un usuario con ese email
    existing_user_by_email = User.query.filter_by(email=email).first()
    if existing_user_by_email:
        # Si el email ya está en uso, no intentamos crear el usuario
        # y retornamos None o levantamos una excepción personalizada
        raise ValueError("El email ya está registrado, mi llave.")

    # Luego, verificamos si ya existe un usuario con ese username (si también es único)
    existing_user_by_username = User.query.filter_by(username=username).first()
    if existing_user_by_username:
        raise ValueError("El nombre de usuario ya está en uso, parcero.")

    hashed_password = generate_password_hash(password)
    user = User(username=username, email=email, password=hashed_password)
    db.session.add(user)
    
    try:
        db.session.commit()
        return user
    except IntegrityError:
        # Esto captura cualquier otra violación de unicidad que se haya colado
        db.session.rollback()
        raise ValueError("Error de integridad de datos. Posiblemente un valor duplicado inesperado.")
    except Exception as e:
        db.session.rollback()
        raise e # Si es otro tipo de error, lo volvemos a levantar

def verify_user(username, password):
    """
    Verifica si un usuario existe y si la contraseña es correcta.
    """
    user = User.query.filter_by(username=username).first()
    if user and check_password_hash(user.password, password):
        return user
    return None
