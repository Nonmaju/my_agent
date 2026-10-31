import streamlit as st
from langchain.chat_models import init_chat_model

model = init_chat_model("gpt-5.4-mini")

if "messages" not in st.session_state:
    st.session_state.messages = []

st.title("우회챗")

prompt = st.chat_input("여기에 입력하시오.")
if prompt:
    response = model.invoke(prompt)
    st.session_state.messages.append({'role': "user", 'content': prompt})
    st.session_state.messages.append({'role': "ai", 'content': response.content})

for message in st.session_state.messages:
    with st.chat_message(message['role']):
        st.write(message['content'])