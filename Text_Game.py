# Text_Game.py
import streamlit as st
from class_stats import CLASS_STATS   # import the dependency

st.set_page_config(page_title="Class Select", layout="centered")

# --- session state ---
st.session_state.setdefault("chosen_class", None)
st.session_state.setdefault("started", False)

# --- UI ---
st.title("Choose Your Class")

cls = st.selectbox("Class:", list(CLASS_STATS.keys()))

stats = CLASS_STATS[cls]
st.subheader(cls)
st.write(stats["desc"])
st.write(f"HP: {stats['hp']}")
st.write(f"Attack: {stats['attack']}")
st.write(f"Defense: {stats['defense']}")
st.write(f"Speed: {stats['speed']}")

col1, col2 = st.columns(2)
with col1:
    if st.button("Confirm Selection"):
        st.session_state.chosen_class = cls
        st.success(f"Selected: {cls}")

with col2:
    if st.session_state.chosen_class and st.button("Start Adventure"):
        st.session_state.started = True
        st.info(f"Adventure started as {st.session_state.chosen_class}.")

# --- Current Info ---
st.write("---")
st.subheader("Current")
st.write(f"Chosen class: {st.session_state.chosen_class or 'None'}")
st.write(f"Started: {st.session_state.started}")