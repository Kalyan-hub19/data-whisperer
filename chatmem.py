# chatmem.py

from langchain.memory import ConversationBufferMemory
from langchain.schema import HumanMessage, AIMessage
from db import get_history

def load_memory(session_id):
    memory = ConversationBufferMemory(memory_key="chat_history", return_messages=True)
    history = get_history(session_id)

    for user_input, bot_response in history:
        memory.chat_memory.add_user_message(HumanMessage(content=user_input))
        memory.chat_memory.add_ai_message(AIMessage(content=bot_response))

    return memory
