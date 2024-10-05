# app.py
from flask import Flask
from flask_socketio import SocketIO  # Import SocketIO
from apis import agent, chat # Adjust the import based on your file name

app = Flask(__name__)
socketio = SocketIO(app)  # Initialize SocketIO with the Flask app
app.register_blueprint(agent)  # Register the blueprint

# Add a simple event handler for WebSocket
@socketio.on('message')
def handle_message(msg):
    if msg == 'start chat':
        print('Initializing chat client...')
        # Logic to initialize the chat client goes here
        chat_instance = chat.Chat()  # Assuming agent_service is defined elsewhere
    else:
        print('Received message: ' + msg)

if __name__ == '__main__':
    socketio.run(app, debug=True)  # Use socketio.run instead of app.run