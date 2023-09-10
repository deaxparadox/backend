from channels.generic.websocket import JsonWebsocketConsumer

"""
This is the default source consumer
"""
class JsonConsumer(JsonWebsocketConsumer):
    def receive_json(self, content, **kwargs):
        print("Recevied: ", content)
        return super().receive_json(content, **kwargs)
    
    def send_json(self, content, close=False):
        print("Send: ", content)
        return super().send_json(content, close)
    


"""
Custom JSON consumer
"""
class CustomJsonConsumer(JsonWebsocketConsumer):
    def receive_json(self, content, **kwargs):
        print("Recevied: ", content)
        # return super().receive_json(content, **kwargs)
        
        content["message"] = content["message"] + ", We hear you!"
        print("Send: ", content)

        super().send_json(content=content, close=False)
    