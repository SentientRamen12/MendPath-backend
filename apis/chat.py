from services.agentService import AgentService

class Chat:
    def __init__(self):
        self.agent_service = AgentService()
        # Initialize any other necessary attributes here

    def handle_socket_message(self, message):
        # Process the incoming socket message
        print("Received message:", message)
        # Add additional processing logic here
        # You can call agent_service methods here if needed
        
