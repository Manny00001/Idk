import streamlit as st

st.set_page_config(page_title="Choice Adventure", layout="centered")

# --- Game state ---
if "scene" not in st.session_state:
    st.session_state.scene = "start"

def go(scene):
    st.session_state.scene = scene

# --- Game scenes ---
def start():
    st.title("🏚️ The Abandoned House")
    st.write("You enter a dark, creaky house. A strange noise echoes in the hall...")
    if st.button("🔦 Run away"):
        go("run")
    if st.button("🕵️ Hide behind furniture"):
        go("hide")

def run():
    st.title("🏃 You Run!")
    st.write("You dash for the door, but it slams shut behind you. The footsteps are getting closer...")
    if st.button("⚔️ Fight"):
        go("fight")
    if st.button("🔒 Look for another exit"):
        go("exit")

def hide():
    st.title("🤫 You Hide")
    st.write("You crouch behind a dusty sofa. The footsteps pause. Someone whispers your name...")
    if st.button("🏃 Jump out and run"):
        go("run")
    if st.button("😱 Stay hidden"):
        go("caught")

def fight():
    st.title("⚔️ The Fight")
    st.write("You grab a broken chair leg and swing. A shadowy figure lunges!")
    if st.button("🏆 You win"):
        go("win")
    if st.button("💀 You lose"):
        go("lose")

def exit():
    st.title("🚪 Another Exit")
    st.write("You find a cellar door. It's unlocked...")
    if st.button("⬇️ Go down"):
        go("cellar")
    if st.button("🔙 Go back"):
        go("start")

def cellar():
    st.title("🕳️ The Cellar")
    st.write("The stairs creak as you descend into darkness...")
    if st.button("👣 Keep going"):
        go("mystery")
    if st.button("⬆️ Go back up"):
        go("start")

def caught():
    st.title("👤 Caught!")
    st.write("A cold hand grabs your shoulder. Game over.")
    if st.button("🔁 Restart"):
        go("start")

def win():
    st.title("🏆 Victory!")
    st.write("You defeated the figure and escaped the house alive!")
    if st.button("🔁 Play again"):
        go("start")

def lose():
    st.title("💀 Defeat")
    st.write("The figure overpowers you. Darkness consumes everything.")
    if st.button("🔁 Try again"):
        go("start")

def mystery():
    st.title("❓ Mystery Ending")
    st.write("You stumble upon a glowing door... To be continued!")
    if st.button("🔁 Restart"):
        go("start")

# --- Run current scene ---
scenes = {
    "start": start,
    "run": run,
    "hide": hide,
    "fight": fight,
    "exit": exit,
    "cellar": cellar,
    "caught": caught,
    "win": win,
    "lose": lose,
    "mystery": mystery,
}
scenes[st.session_state.scene]()