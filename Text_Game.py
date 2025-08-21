# app.py
import streamlit as st
from datetime import datetime

st.set_page_config(page_title="Mini Text Adventure", layout="centered")

# --- simple brain you can swap out ---
def respond(user_msg: str) -> str:
    # TODO: replace with your own logic / LLM call
    if any(w in user_msg.lower() for w in ["exit","quit","bye"]):
        return "You can close the tab or start a new run from the sidebar."
    if "look" in user_msg.lower():
        return "You see a dim corridor, a rusty door to the north, and footprints leading east."
    if "open" in user_msg.lower():
        return "The door creaks open. It’s dark inside. Something moves."
    return f"(echo) {user_msg}"

# --- state ---
if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role":"game", "text":"Welcome to the Text Game! Type anything and I’ll respond."}
    ]

# --- sidebar controls ---
with st.sidebar:
    st.title("Controls")
    if st.button("🔁 New Run"):
        st.session_state.messages = [{"role":"game","text":"New run started."}]
    st.caption(f"Time: {datetime.now().strftime('%H:%M:%S')}")

# --- chat display ---
st.title("Mini Text Adventure")
for m in st.session_state.messages:
    if m["role"] == "user":
        with st.chat_message("user"):
            st.write(m["text"])
    else:
        with st.chat_message("assistant"):
            st.write(m["text"])

# --- input box ---
user_msg = st.chat_input("You:")
if user_msg:
    st.session_state.messages.append({"role":"user","text":user_msg})
    with st.chat_message("user"):
        st.write(user_msg)

    reply = respond(user_msg)
    st.session_state.messages.append({"role":"game","text":reply})
    with st.chat_message("assistant"):
        st.write(reply)
