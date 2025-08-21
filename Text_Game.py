def text_game():
    print("Welcome to the Text Game! Type anything and I'll respond.")
    while True:
        user_input = input("You: ")
        if user_input.lower() in ["exit", "quit", "bye"]:
            print("Game: Goodbye!")
            break
        else:
            print(f"Game: {user_input}")

if __name__ == "__main__":
    text_game()
