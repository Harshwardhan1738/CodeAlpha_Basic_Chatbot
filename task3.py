import nltk
from nltk.chat.util import Chat, reflections

# Define a set of pairs for pattern matching and responses
pairs = [
    [
        r"hi|hello|hey",
        ["Hello! How can I assist you today?", "Hi there! What's on your mind?", "Hey! How can I help?"]
    ],
    [
        r"(.*) your name?",
        ["I'm ChatBot, your virtual assistant!", "You can call me ChatBot."]
    ],
    [
        r"how are you(.*)?",
        ["I'm just a program, but I'm here to help you!", "I'm doing great, thanks for asking. How about you?"]
    ],
    [
        r"(.*) help (.*)",
        ["Sure, I'm here to help! What do you need assistance with?", "I'd be happy to help. Please tell me more."]
    ],
    [
        r"(.*) weather (.*)",
        ["I'm not connected to live weather services right now, but you can check a weather app!", "I recommend using a weather website for accurate updates."]
    ],
    [
        r"quit",
        ["Goodbye! Have a great day!", "See you later! Take care!"]
    ],
    [
        r"(.*)",
        ["That's interesting! Tell me more.", "I'm not sure I understand, but I'm here to listen.", "Can you explain that in more detail?"]
    ]
]

def chatbot():
    print("Hi, I'm your chatbot! Type 'quit' to exit.")
    chat = Chat(pairs, reflections)
    chat.converse()

if __name__ == "__main__":
    chatbot()
