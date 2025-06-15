# backend/main.py

from app import create_app, socketio  # 👈 importante: importar desde app/__init__.py

app = create_app()

if __name__ == '__main__':
    socketio.run(app, debug=True, port=5000)
