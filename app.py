import streamlit as st
import tempfile
import uuid
from agent import get_agent
from db import init_db, save_chat


st.set_page_config(page_title="DataWhisperer", layout="wide")

if "session_id" not in st.session_state:
    st.session_state.session_id = str(uuid.uuid4())
if "history" not in st.session_state:
    st.session_state.history = []

st.title(" DATA WHISPERER")
st.markdown(" Ask questions about your CSV data using AI")

uploaded_file = st.file_uploader("📄 Upload a CSV file", type=["csv"])

if uploaded_file:
    with tempfile.NamedTemporaryFile(delete=False, suffix=".csv") as tmp:
        tmp.write(uploaded_file.read())
        tmp_path = tmp.name

    agent = get_agent(tmp_path, st.session_state.session_id)

    user_input = st.chat_input("Ask your CSV a question...")
    if user_input:
        with st.spinner("Thinking..."):
            response = agent.run(user_input)
            st.session_state.history.append((user_input, response))
            save_chat(st.session_state.session_id, user_input, response)

    for q, a in st.session_state.history:
        with st.chat_message("user"): st.write(q)
        with st.chat_message("assistant"): st.write(a)
