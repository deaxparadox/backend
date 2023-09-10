from channels.consumer import SyncConsumer


class BackgroundWorkerTest(SyncConsumer):
    def test_print(self, message):
        print(message)
        print("Test: ", message["text"])

        self.send("I got your message")

    # def websocket_connect(self, event):
    #     self.send({
    #         "type": "websocket.accept",
    #     })

    # def websocket_receive(self, event):
    #     self.send({
    #         "type": "websocket.send",
    #         "text": event["text"],
    #     })

    