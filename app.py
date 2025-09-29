from fastapi import FastAPI, WebSocket, WebSocketDisconnect, HTTPException
from fastapi.responses import HTMLResponse
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List, Dict
import uuid
from datetime import datetime

app = FastAPI()

# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Models
class ThreadCreate(BaseModel):
    title: str
    content: str
    category: str

class ReplyCreate(BaseModel):
    content: str
    name: str

# In-memory storage
threads = []
global_chat_messages = []
active_users: Dict[str, dict] = {}

# WebSocket manager
class ConnectionManager:
    def __init__(self):
        self.active_connections: Dict[str, WebSocket] = {}

    async def connect(self, websocket: WebSocket, user_id: str):
        await websocket.accept()
        self.active_connections[user_id] = websocket

    def disconnect(self, user_id: str):
        if user_id in self.active_connections:
            del self.active_connections[user_id]

    async def broadcast(self, message: dict):
        dead_users = []
        for user_id, connection in self.active_connections.items():
            try:
                await connection.send_json(message)
            except:
                dead_users.append(user_id)
        for u in dead_users:
            self.disconnect(u)

manager = ConnectionManager()

# Routes
@app.get("/", response_class=HTMLResponse)
async def get_html():
    with open("index.html", "r", encoding="utf-8") as f:
        return f.read()

@app.get("/api/threads")
async def get_threads():
    return {"threads": threads}

@app.post("/api/threads")
async def create_thread(thread: ThreadCreate):
    new_thread = {
        "id": str(uuid.uuid4()),
        "title": thread.title,
        "content": thread.content,
        "category": thread.category,
        "created_at": datetime.now().isoformat(),
        "replies": []
    }
    threads.append(new_thread)

    await manager.broadcast({"type": "new_thread", "thread": new_thread})
    return {"status": "ok", "thread": new_thread}

@app.post("/api/threads/{thread_id}/reply")
async def add_reply(thread_id: str, reply: ReplyCreate):
    for thread in threads:
        if thread["id"] == thread_id:
            new_reply = {
                "id": str(uuid.uuid4()),
                "content": reply.content,
                "name": reply.name,
                "created_at": datetime.now().isoformat()
            }
            thread["replies"].append(new_reply)

            await manager.broadcast({
                "type": "new_reply",
                "thread_id": thread_id,
                "reply": new_reply
            })

            return {"status": "ok", "reply": new_reply}
    raise HTTPException(status_code=404, detail="Thread not found")

@app.get("/api/threads/{thread_id}")
async def get_thread(thread_id: str):
    for thread in threads:
        if thread["id"] == thread_id:
            return thread
    raise HTTPException(status_code=404, detail="Thread not found")

@app.get("/api/chat/messages")
async def get_chat_messages():
    return {"messages": global_chat_messages[-100:]}

@app.websocket("/ws/{user_id}")
async def websocket_endpoint(websocket: WebSocket, user_id: str):
    await manager.connect(websocket, user_id)
    active_users[user_id] = {"id": user_id, "connected_at": datetime.now().isoformat()}

    await manager.broadcast({
        "type": "user_joined",
        "user_id": user_id,
        "active_users": len(active_users)
    })

    try:
        while True:
            data = await websocket.receive_json()
            if data["type"] == "chat_message":
                message = {
                    "id": str(uuid.uuid4()),
                    "user_id": user_id,
                    "name": data.get("name", "Guest"),
                    "message": data["message"],
                    "timestamp": datetime.now().isoformat()
                }
                global_chat_messages.append(message)
                await manager.broadcast({"type": "chat_message", "message": message})

    except WebSocketDisconnect:
        manager.disconnect(user_id)
        if user_id in active_users:
            del active_users[user_id]
        await manager.broadcast({
            "type": "user_left",
            "user_id": user_id,
            "active_users": len(active_users)
        })

@app.get("/api/stats")
async def get_stats():
    return {
        "active_users": len(active_users),
        "total_threads": len(threads),
        "total_messages": len(global_chat_messages)
    }

if __name__ == "__main__":
    import uvicorn
    import os
    port = int(os.environ.get("PORT", 8000))
    uvicorn.run("app:app", host="0.0.0.0", port=port)

