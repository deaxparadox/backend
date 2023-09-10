import websocket

url: str = "ws://localhost:8000/ws/chat/dsffa/"

def on_message(ws, message):
    print(message)


def on_error(ws, error):
    print(f"Error: {error}")


wsapp = websocket.WebSocketApp(
    url, 
    on_message=on_message,
    on_error=on_error
)

wsapp.run_forever()
