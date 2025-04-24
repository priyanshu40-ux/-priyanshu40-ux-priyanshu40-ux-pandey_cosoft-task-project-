def chatbot():
    print("Chatbot: Hello! I'm your friendly chatbot. Type 'bye' to exit.")
    
    while True:
        user_input = input("You: ").lower()

        # Exit condition
        if "bye" in user_input:
            print("Chatbot: Goodbye! Have a great day!")
            break

        # Responses based on rules
        elif "hello" in user_input or "hi" in user_input:
            print("Chatbot: Hello there! How can I help you today?")
        
        elif "how are you" in user_input:
            print("Chatbot: I'm just a bot, but I'm doing great! Thanks for asking.")
        
        elif "your name" in user_input:
            print("Chatbot: I'm a simple rule-based chatbot created by you!")
        
        elif "what can you do" in user_input:
            print("Chatbot: I can respond to basic greetings and questions. Try saying 'hello' or 'how are you'.")
        
        elif "help" in user_input:
            print("Chatbot: Sure, I'm here to help. You can ask me simple questions like 'What's your name?' or say 'hi'.")
        
        else:
            print("Chatbot: I'm not sure how to respond to that. Try asking something else.")

# Run the chatbot
chatbot()
