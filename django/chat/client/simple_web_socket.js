const WebSocket = require('ws');

let BASE_URL = "ws://localhost:8000"


const generateURL = function() {
    return BASE_URL + `/ws/chat/lobby/`
} 

// const url = generateURL();
// console.log(url)
const socket = new WebSocket("ws://127.0.0.1:8000/ws/chat/dsffa/", {
    "origin": "http://127.0.0.1:8000"
});

socket.onmessage = async (e) => {
    console.log(e.data);
}

socket.onerror = async (e) => {
    console.log(e)
}

socket.onclose = async (e) => {
    console.log(e)
}
socket.onopen = async (e) => {
    console.log("connected!")
    setInterval(function() {
        socket.send(JSON.stringify({
            "message": "Hi to everyone!"
        }));
    }, 2000)
}
