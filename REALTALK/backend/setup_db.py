from app import create_app, db

def setup_database():
    app = create_app()
    
    with app.app_context():
        # ¡¡IMPORTANTE: Esta línea borra TODAS las tablas en la base de datos conectada!!
        # Úsela con EXTREMO cuidado en entornos de producción, solo en desarrollo.
        print("Intentando borrar TODAS las tablas existentes...")
        db.drop_all()
        print("Tablas borradas (si existían).")
        
        # Esto crea todas las tablas según sus modelos actuales.
        print("Creando todas las tablas según el modelo actual (incluyendo 'email')...")
        db.create_all()
        print("¡Base de datos y tablas creadas exitosamente!")
        
        # Opcional: crear usuarios de prueba
        from app.models.user import User
        from werkzeug.security import generate_password_hash
        
        if not User.query.filter_by(username='test1').first():
            user1 = User(
                username='test1', 
                email='test1@example.com', 
                password=generate_password_hash('password123')
            )
            user2 = User(
                username='test2', 
                email='test2@example.com', 
                password=generate_password_hash('password123')
            )
            
            db.session.add(user1)
            db.session.add(user2)
            db.session.commit()
            print("Usuarios de prueba creados!")

if __name__ == '__main__':
    setup_database()