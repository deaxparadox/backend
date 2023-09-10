import json 
import typing

from asgiref.sync import async_to_sync
from channels.generic.websocket import WebsocketConsumer


def json_loads(data: typing.Any | None):
    return json.loads(data)

def json_dumps(data: typing.Any | None):
    return json.dumps(data)
import json

from asgiref.sync import async_to_sync
from channels.generic.websocket import WebsocketConsumer


class ChatConsumer(WebsocketConsumer):
    def websocket_connect(self, message):
        self.base_send({"type": "websocket.accept", "accept": True})

    def connect(self):
        self.room_name = self.scope["url_route"]["kwargs"]["room_name"]
        self.room_group_name = f"chat_{self.room_name}"

        # self.send({"accept": True})   

        # Join room group
        async_to_sync(self.channel_layer.group_add)(
            self.room_group_name, self.channel_name
        )
        

        self.accept()

    def disconnect(self, close_code):
        # Leave room group
        async_to_sync(self.channel_layer.group_discard)(
            self.room_group_name, self.channel_name
        )

    # Receive message from WebSocket
    def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json["message"]

        print(message)

        # Send message to room group
        async_to_sync(self.channel_layer.group_send)(
            self.room_group_name, {"type": "chat.message", "message": message}
        )

    # Receive message from room group
    def chat_message(self, event):
        message = event["message"]

        # Send message to WebSocket
        self.send(text_data=json.dumps({"message": message}))

class UserChatConsumer(WebsocketConsumer):
    def connect(self):
        print(self.scope["url_route"]["kwargs"])
        self.room_name = self.scope["url_route"]["kwargs"]["room_name"]
        self.user_name = self.scope["url_route"]["kwargs"]["user_name"]
        self.room_group_name = f"chat_{self.room_name}"

        details = f"User name: {self.user_name}\nChannel name: {self.channel_name}\nChannel layer: {self.channel_layer}\n"
        print(details)

        # Join room group
        async_to_sync(self.channel_layer.group_add)(
            self.room_group_name, self.channel_name
        )

        self.accept()

    def disconnect(self, code):
        # Leave room group
        async_to_sync(self.channel_layer.group_discard)(
            self.room_group_name, self.channel_name
        )

    # Receive message from WebSocket
    def receive(self, text_data):
        text_data_json = json_loads(text_data)
        message = text_data_json["message"]


        self.channel_layer.send(
            "test-message",
            {
                "type": "test.print",
                "text": "Ready for fun",
            }
        )

        # Send message to room group
        async_to_sync(self.channel_layer.group_send)(
            self.room_group_name, {
                "type": "chat.message",
                "message": message
            }
        )

    # Receive message from room group
    def chat_message(self, event):
        message = event["message"]

        # Send message to WebSocket
        self.send(text_data=json_dumps({"message": message}))