# app.py
import streamlit as st
from units import ROSTER   # import stats from separate script

st.set_page_config(page_title="Choose Team", layout="centered")

# --- state ---
st.session_state.setdefault("team", [])
st.session_state.setdefault("started", False)

st.title("Pick Your Team")

# Dropdown
choice = st.selectbox("Choose your starter:", list(ROSTER.keys()))

if st.button("Add to Team"):
    st.session_state.team = [ROSTER[choice].copy()]
    st.success(f"Added {choice} to your team.")

st.write("---")
st.subheader("Current Team")

if not st.session_state.team:
    st.caption("No one selected yet.")
else:
    for m in st.session_state.team:
        st.write(f"{m['name']} — {m['class']} (Lv {m['level']})")
        st.write(f"HP: {m['hp']}")
        st.write(f"Attack: {m['attack']}")
        st.write(f"Defense: {m['defense']}")

if st.session_state.team and st.button("Start Adventure ▶"):
    st.session_state.started = True
    st.success("Adventure started!")