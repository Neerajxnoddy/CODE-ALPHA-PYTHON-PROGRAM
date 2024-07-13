import random

# Dictionary of responses
responses = {
    "hi": "Hello! How can I help you today?",
    "hello": "Hi there! What can I do for you?",
    "how are you": "I'm good, thank you for asking!",
    "bye": "Goodbye!",
    "thanks": "You're welcome!",
    "what's your name?": "I'm just a chat bot.",
    "who are you?": "I'm a chat bot created to assist you.",
    "what can you do?": "I can provide information and answer questions.",
    "what is your purpose?": "My purpose is to assist and provide information.",
    "how old are you?": "I don't have an age. I'm just a program.",
    "where are you from?": "I'm from the cloud!",
    "tell me a joke": "Why don't skeletons fight each other? They don't have the guts.",
    "tell me something interesting": "Did you know that honey never spoils?",
    "default": "Sorry, I didn't understand that. Can you ask me something else?"
}

# Function to generate response
def generate_response(user_input):
    # Convert user input to lowercase
    user_input = user_input.lower()
    # Check if user input exists in responses, else return default response
    return responses.get(user_input, responses["default"])

# Chatting interface
def chat():
    print("ChatBot: Hi! How can I assist you today?")
    while True:
        user_input = input("You: ")
        if user_input.lower() == 'bye':
            print("ChatBot: Goodbye!")
            break
        else:
            response = generate_response(user_input)
            print("ChatBot:", response)

if __name__ == "__main__":
    chat()
