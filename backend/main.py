# backend/main.py
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from chatbot import get_response  # Your Hugging Face chatbot wrapper

app = FastAPI(title="MindEase Chatbot Backend")

# Enable CORS so frontend can communicate with backend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # For local testing; restrict to your frontend URL in production
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def read_root():
    """
    Root endpoint to check if backend is running.
    """
    return {"message": "MindEase backend is running!"}

@app.get("/chat")
def chat(message: str):
    """
    Receives a user message via query parameter 'message'
    and returns the chatbot's response.
    Example: GET /chat?message=Hello
    """
    response = get_response(message)
    return {"response": response}
