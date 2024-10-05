from flask import Blueprint, jsonify
from flask_socketio import SocketIO, emit  # Import SocketIO and emit
from services.agentService import AgentService

agent_blueprint = Blueprint('agent', __name__)  # Create a blueprint for the agent

# New WebSocket route
@agent_blueprint.route('/agent', methods=['GET'])
def get_agent():
    agent_service = AgentService()
    agent_service.create_connection()
    agent_service.stream_text("Hello, Hume!")
    return jsonify({"message": "Agent details retrieved and text streamed."})

if __name__ == '__main__':
    agent_blueprint.run(debug=True)