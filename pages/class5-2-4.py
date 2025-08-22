import streamlit as st
import openai

openai.api_key = st.secrets["OPENAI_API_KEY"]
ss = st.session_state
if "history" not in ss:
    ss.history = [{"role": "system", "content": "please use chinese to respond"}]

col_chat, col_clear = st.columns([9,1])
with col_clear:
    if st.button("🗑️"):
        ss.history = [{"role": "system", "content": "please use chinese to respond"}]
        st.rerun()


for message in ss.history:
    if message["role"] == "user":
        st.chat_message("user").write(message["content"])
    elif message["role"] == "assistant":
        st.chat_message("assistant").write(message["content"])

prompt = st.chat_input("請輸入您的問題...")
if prompt:
    ss.history.append({"role": "user", "content": prompt})
    
    response = openai.chat.completions.create(
        model="gpt-5",
        messages=ss.history,
    )

    assistant_message = response.choices[0].message.content
    ss.history.append({"role": "assistant", "content": assistant_message})
    st.rerun()