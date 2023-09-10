import { WebSocketClient, StandardWebSocketClient } from "https://deno.land/x/websocket@v0.1.4/mod.ts";

const endpoint = "ws://127.0.0.1:8000/ws/chat/dsffa/";

const ws: WebSocketClient = new StandardWebSocketClient(endpoint);




ws.on("open", function() {
  console.log("ws connected!");
  ws.send(JSON.stringify(
    {
        "message": "this is from deno client."
    }
  ));
});

ws.on("message", function (message: string) {
  console.log(message);
});