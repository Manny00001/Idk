# app.py
import os, streamlit as st
from openai import OpenAI

# ====== CONFIG ======
MODEL = "gpt-4o-mini"  # fast + cheap
PAGE_TITLE = "Pocket Adventure"

# Get key from Streamlit secrets or env
API_KEY = st.secrets.get("OPENAI_API_KEY") or os.getenv("OPENAI_API_KEY")
if not API_KEY:
    st.error("Set OPENAI_API_KEY via streamlit secrets or environment variable.")
    st.stop()
client = OpenAI(api_key=API_KEY)

st.set_page_config(page_title=PAGE_TITLE, layout="wide")

# ====== STATE ======
def init_state():
    st.session_state.setdefault("started", False)
    st.session