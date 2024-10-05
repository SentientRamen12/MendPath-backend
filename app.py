# app.py
from flask import Flask, request  # Import request to access session ID
from flask_socketio import SocketIO, emit
from apis import agent, chat
import json

app = Flask(__name__)
socketio = SocketIO(app)
app.register_blueprint(agent)

# Store connected clients with their chat clients
clients = {}  # Dictionary to hold connected clients and their chat clients

@socketio.on('connect')
async def handle_connect():
    client_id = request.sid  # Get the unique session ID for the client
    clients[client_id] = {'status': 'connected', 'chat_client': create_chat_client()}  # Store client info with a new chat client
    print(f'Client {client_id} connected.')

@socketio.on('disconnect')
async def handle_disconnect():
    client_id = request.sid  # Get the unique session ID for the client
    if client_id in clients:
        del clients[client_id]  # Remove client info on disconnect
        print(f'Client {client_id} disconnected.')

@socketio.on('message')
async def handle_message(msg):
    data = json.loads(msg)
    client_id = request.sid  # Get the unique session ID for the client
    if data.get('event') == 'send text':
        body_message = data.get('body')
        print(f'Received text message: {body_message}')
        # Logic to handle the text message and trigger chat goes here
        chat_client = clients[client_id]['chat_client']  # Access the specific chat client for this session
        output = await chat_client.handle_text_message(body_message)
        emit('message', {'event': 'receive text', 'body': output})
        # Use chat_client to process the message

def create_chat_client():
    # Function to create and return a new chat client instance
    chat_client = chat.Chat()
    return chat_client

if __name__ == '__main__':
    socketio.run(app, debug=True)