import streamlit as st

st.chat_message("user").write("this is user's message")
st.chat_message("assistant").write("this is AI's message")

history = [
    {"role": "user", "content": "hello, AI!"},
    {"role": "assistant", "content": "hello, what can I help you with?"},
    {"role": "user", "content": "how to make a cake?"},
    {
        "role": "assistant",
        "content": "st.chat_message()"
    },
]

for message in history:
    if message["role"] == "user":
        st.chat_message("user").write(message["content"])
    elif message["role"] == "assistant":
        st.chat_message("assistant").write(message["content"])