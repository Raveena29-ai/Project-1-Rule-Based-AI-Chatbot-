print("Welcome to AI Chatbot!")

while True:
    user_input = input("You: ").lower()

    if user_input == "hi":
        print("Bot: Hello!")
    elif user_input == "how are you":
        print("Bot: I am fine.")
    elif user_input == "bye":
        print("Bot: Goodbye!")
        break
    else:
        print("Bot: Sorry, I don't understand.")