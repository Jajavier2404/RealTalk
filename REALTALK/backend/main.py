# backend/main.py
from flask import Flask, jsonify
from flask_cors import CORS
from flask_socketio import SocketIO

app = Flask(__name__)
CORS(app)
socketio = SocketIO(app, cors_allowed_origins="*")

@app.route('/')
def index():
    return jsonify({"mensaje": "Hola desde Flask 😎"})

if __name__ == '__main__':
    socketio.run(app, debug=True, port=5000)
