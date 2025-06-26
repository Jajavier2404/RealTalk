from flask_socketio import emit, join_room
from app import socketio
from .controller import save_message

@socketio.on('send_message')
def handle_message(data):
    msg = save_message(data['sender_id'], data['content'])
    emit('receive_message', msg.to_dict(), broadcast=True)
