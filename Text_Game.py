# class_select.py
import streamlit as st

st.set_page_config(page_title="Choose Your Class", layout="centered")

# --- class data ---
CLASSES = {
    "Mage":    {"hp": 80,  "attack": 40, "defense": 20, "description": "Masters of arcane power, fragile but deal high magic damage."},
    "Warrior": {"hp": 120, "attack": 35, "defense": 30, "description": "Balanced fighters with strong melee combat skills."},
    "Healer":  {"hp": 90,  "attack": 20, "defense": 25, "description": "Support allies by healing and keeping the team alive."},
    "Tank":    {"hp": 160, "attack": 25, "defense": 45, "description": "Absorb damage and protect others with high defense."},
}

# --- state ---
st.session_state.setdefault("player_class", None)

st.title("Pick Your Class")

# Dropdown to choose class
choice = st.selectbox("Choose your class:", list(CLASSES.keys()))

if st.button("Confirm Choice"):
    st.session_state.player_class = choice
    st.success(f"You chose {choice}!")

st.write("---")
st.subheader("Current Selection")

if not st.session_state.player_class:
    st.caption("No class selected yet.")
else:
    c = CLASSES[st.session_state.player_class]
    st.write(f"Class: {st.session_state.player_class}")
    st.write(f"HP: {c['hp']}")
    st.write(f"Attack: {c['attack']}")
    st.write(f"Defense: {c['defense']}")
    st.write(c["description"])