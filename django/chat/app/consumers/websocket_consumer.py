import json 

from channels.generic.websocket import (
    WebsocketConsumer, 
    AsyncWebsocketConsumer,
    async_to_sync
)

# from polls.models import Question

# his wraps the verbose plain-ASGI message sending and receiving 
# into handling that just deals with text and binary frames:

class MyConsmer(WebsocketConsumer):
    groups = ["broadcast"]

    def connect(self):
        # Called on connection.
        # To accept the connection call:
        self.accept()

        # Or accept the connection and specify a chosen subprotocol.
        # A list of subprotocols specified by the connecting client
        # will be available in self.scope['subprotocols']
        # self.accept("subprotocol")
        
        # To reject the connection, call:
        # self.close()

    def receive(self, text_data=None, bytes_data=None):
        # Called with either text_data or bytes_data for each frame
        # You can call:
        self.send(text_data="Hello world!")

        # # Or, to send a binary frame:
        # self.send(bytes_data="Hello world!")
        
        # # Want to force-close the connection? Call:
        # self.close()
        
        # # Or add a custom WebSocket error code!
        # self.close(code=4123)

    def disconnect(self, close_code):
        # Called when the socket closes
        super().disconnect(code=close_code)




class SimpleConsumer(WebsocketConsumer):
    """
    This is a synchronous WebSocket consumer that accepts all connections, 
    receives messages from its client, and echos those messages back to the 
    same client.
    """
    def connect(self):
        self.accept()

    def disconnect(self, code):
        pass 


    def receive(self, text_data=None, bytes_data=None):
        text_data_json = json.loads(text_data)
        message = text_data_json["message"]

        

        # question = self.get_questions()
        # question = ""
        # print(question)

        self.send(text_data=json.dumps({"message": message}))

    # @database_sync_to_async
    # def get_questions(self):
    #     return Question.objects.all()
    


# class AsyncSimpleConsumer(AsyncWebsocketConsumer):
#     async def connect(self):
#         self.accept()