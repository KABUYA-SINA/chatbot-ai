"""
FastAPI interface for the chatbot.

This module exposes the chatbot through HTTP endpoints.
It acts as a thin layer above ChatEngine.
"""

from fastapi import FastAPI
from pydantic import BaseModel

from chatbot.engine import ChatEngine


app = FastAPI(title="Chatbot API", version="1.0.0")

engine = ChatEngine(test_mode=False)


# ------------------------------------------------------------
# Request model
# ------------------------------------------------------------

class ChatRequest(BaseModel):
    message: str


# ------------------------------------------------------------
# Routes
# ------------------------------------------------------------

@app.get("/")
def home():
    """
    Health check endpoint.
    """
    return {
        "status": "ok",
        "message": "Chatbot API is running"
    }


@app.post("/chat")
def chat(req: ChatRequest):
    """
    Main chat endpoint.
    """

    response = engine.process(req.message)

    return {
        "response": response
    }