from services.agentService import AgentService

class WebSocketInterface:
    def on_open(self):
        # Handle the opening of the WebSocket connection
        print("WebSocket connection opened.")

    def on_message(self, message):
        # Handle incoming messages
        print(f"Message received: {message}")

    def on_close(self):
        # Handle the closing of the WebSocket connection
        print("WebSocket connection closed.")

    def on_error(self, error):
        # Handle errors
        print(f"WebSocket error: {error}")

class Chat:
    def __init__(self):
        self.websocket_interface = WebSocketInterface()
        
        # Initialize any other necessary attributes here

    
    async def connect_to_chat(self):
        # Open the WebSocket connection with the configuration options and the interface's handlers
        async with client.empathic_voice.chat.connect_with_callbacks(
            options=options,
            on_open=self.websocket_interface.on_open,
            on_message=self.websocket_interface.on_message,  # Handle incoming messages
            on_close=self.websocket_interface.on_close,      # Handle connection closure
            on_error=self.websocket_interface.on_error,      # Handle errors
        ):
            # ... handle the connection ...
            await self.websocket_interface.listen()  # Start listening for messages