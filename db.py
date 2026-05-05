# mongo_db.py

from pymongo import MongoClient
import os
from dotenv import load_dotenv

load_dotenv()
MONGO_URI = os.getenv("MONGODB_URI")
client = MongoClient(MONGO_URI)
db = client["datawhisperer"]
collection = db["chat_history"]

def init_db():
    return collection

def save_chat(session_id, user_input, bot_response):
    collection.insert_one({
        "session_id": session_id,
        "user_input": user_input,
        "bot_response": bot_response
    })

def get_history(session_id):
    history = collection.find({"session_id": session_id})
    return [(item["user_input"], item["bot_response"]) for item in history]
