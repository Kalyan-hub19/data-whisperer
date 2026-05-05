import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_experimental.agents import create_csv_agent
from chatmem import load_memory

load_dotenv()

def get_agent(csv_path, session_id):
    llm = ChatOpenAI(
        base_url="https://api.together.xyz/v1",
        api_key=os.getenv("TOGETHER_API_KEY"),
        model="mistralai/Mixtral-8x7B-Instruct-v0.1",
        temperature=0.3
    )

    memory = load_memory(session_id)

    return create_csv_agent(
        llm=llm,
        path=csv_path,
        memory=memory,
        verbose=True,
        allow_dangerous_code=True
    )
