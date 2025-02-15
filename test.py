from typing import Annotated

import uvicorn
from fastapi import (
    Cookie,
    Depends,
    FastAPI,
    Query,
    WebSocket,
    WebSocketException,
    status, Path,
)
from fastapi.responses import HTMLResponse

active_connections: dict[str, dict[str, WebSocket]] = {}

app = FastAPI()

html = """
<!DOCTYPE html>
<html>
    <head>
        <title>Chat</title>
    </head>
    <body>
        <h1>WebSocket Chat</h1>
        <form action="" onsubmit="sendMessage(event)">
            <label>chat: <input type="text" id="chat" autocomplete="off" value="some-key-token"/></label>
            <label>username: <input type="text" id="username" autocomplete="off" value="username"/></label>
            <button onclick="connect(event)">Connect</button>
            <hr>
            <label>Message: <input type="text" id="messageText" autocomplete="off"/></label>
            <button>Send</button>
        </form>
        <ul id='messages'>
        </ul>
        <script>
            var ws = null;
            function connect(event) {
                var chat = document.getElementById("chat").value;
                var username = document.getElementById("username").value;
                ws = new WebSocket("wss://todoserviceapi-test.up.railway.app/items/" + chat + "/" + username + "/ws");
                ws.onmessage = function(event) {
                    var messages = document.getElementById('messages');
                    var message = document.createElement('li');
                    var content = document.createTextNode(event.data);
                    message.appendChild(content);
                    messages.appendChild(message);
                };
                event.preventDefault();
            }
            function sendMessage(event) {
                var input = document.getElementById("messageText");
                if (ws && ws.readyState === WebSocket.OPEN) {
                    ws.send(input.value);
                } else {
                    alert('WebSocket connection is not open.');
                }
                input.value = '';
                event.preventDefault();
            }
        </script>
    </body>
</html>

"""


@app.get("/")
async def get():
    return HTMLResponse(html)


@app.websocket("/items/{chat}/{username}/ws")
async def websocket_endpoint(
    *,
    websocket: WebSocket,
    chat: Annotated[str, Path()],
    username: Annotated[str, Path()],
):
    await websocket.accept()

    if chat not in active_connections:
        active_connections[chat] = {}

    active_connections[chat][username] = websocket

    while True:
        data = await websocket.receive_text()
        await websocket.send_text(data)
        for user, socket in active_connections[chat].items():
            if user == username:
                continue
            else:
                await socket.send_text(data)



if __name__ == '__main__':
    uvicorn.run(app)