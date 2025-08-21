# app.py
import streamlit as st

st.set_page_config(page_title="Team Select", layout="centered")

# ---- Options ----
CHARACTERS = ["Gojo", "Sukuna"]   # add more later

# ---- State ----
if "team" not in st.session_state:
    st.session_state.team = []

# ---- UI ----
st.title("👥 Choose Your Team")

# dropdown to select character
choice = st.selectbox("Select a character to add to your team:", CHARACTERS)

if st.button("➕ Add to Team"):
    if choice not in st.session_state.team:
        st.session_state.team.append(choice)
        st.success(f"{choice} added!")
    else:
        st.warning(f"{choice} is already in your team.")

st.divider()
st.subheader("📋 Current Team")
if st.session_state.team:
    for i, member in enumerate(st.session_state.team, 1):
        st.write(f"{i}. {member}")
else:
    st.caption("No team members yet.")