import json 

from channels.generic.websocket import WebsocketConsumer, AsyncWebsocketConsumer
from channels.consumer import SyncConsumer, AsyncConsumer
from channels.db import database_sync_to_async

# from polls.models import Question


from channels.consumer import SyncConsumer

class EchoConsumer(SyncConsumer):
    """
    This is a very simple WebSocket echo server - it will accept all 
    incoming WebSocket connections, and then reply to all incoming 
    WebSocket text frames with the same text.
    """

    def websocket_connect(self, event):
        self.send({
            "type": "websocket.accept",
        })

    def websocket_receive(self, event):
        event['text'] = "Received: " + event['text']
        self.send({
            "type": "websocket.send",
            "text": event["text"],
        })


class AsyncEchoConsumer(AsyncConsumer):
    async def websocket_connect(self, event):
        await self.send({
            "type": "websocket.accept",
        })
    async def websocket_recevie(self, event):
        await self.send({
            "type": "websocket.send",
            "text": event["text"]
        })