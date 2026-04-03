def chatbot():
    print("🤖 Chatbot: Hello! Type 'bye' to exit.")

    while True:
        user = input("You: ").lower()

        if user == "hello":
            print("Bot: Hi there!")
        elif user == "how are you":
            print("Bot: I'm just code, but I'm doing great!")
        elif user == "your name":
            print("Bot: I'm a simple Python chatbot.")
        elif user == "help":
            print("Bot: You can ask me simple questions!")
        elif user == "i like you":
            print("Bot: I like You So much my friend..")
        elif user == "who are you?":
            print("Bot: I'm an chatbot for answering your questions!..")
        elif user == "whats your name?":
            print("Bot: My Name is CRYTO!..")
        elif user == "bye":
            print("Bot: Goodbye! 👋")
            break
        else:
            print("Bot: Sorry, I don't understand that.")

chatbot()
