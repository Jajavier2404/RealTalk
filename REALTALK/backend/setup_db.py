# setup_db.py
from app import create_app, db

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
    print("¡Base de datos y tablas creadas exitosamente, mi llave!")