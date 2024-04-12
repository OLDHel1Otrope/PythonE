import streamlit as st
import os
import google.generativeai as genai

st.title("gemini-bot")

os.environ['GOOGLE_API_KEY'] = "insertapikeyshere"
genai.configure(api_key=os.environ['GOOGLE_API_KEY'])

model = genai.GenerativeModel('gemini-pro')

if "messages" not in st.session_state:
    st.session_state.messages = [
        {
            "role": "assistant",
            "content": "Ask me Anything"
        }
    ]

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])


def llm_function(query):
    response = model.generate_content(query)

    with st.chat_message("assistant"):
        st.markdown(response.text)

    st.session_state.messages.append(
        {
            "role": "user",
            "content": query
        }
    )

    st.session_state.messages.append(
        {
            "role": "assistant",
            "content": response.text
        }
    )


query = st.chat_input("whats up?")

if query:
    with st.chat_message("user"):
        st.markdown(query)

    llm_function(query)
