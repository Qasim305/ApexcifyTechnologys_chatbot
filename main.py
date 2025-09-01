import json
import random
import os

# File to store chatbot memory
MEMORY_FILE = "chatbot_memory.json"

# Load saved responses if file exists, otherwise use defaults
if os.path.exists(MEMORY_FILE):
    with open(MEMORY_FILE, "r") as f:
        responses = json.load(f)
else:
    responses = {
        "hello": ["Hi!", "Hello there!", "Hey 👋"],
        "hi": ["Hello!", "Hey!", "Hi there!"],
        "hey": ["Hey! How's it going?", "Hey 👋", "Yo!"],
        "how are you": ["I'm fine, thanks!", "Doing great, how about you?"],
        "bye": ["Goodbye! Have a great day!", "See you soon!", "Bye"]
    }

# To Save responses to JSON file
def save_responses():
    with open(MEMORY_FILE, "w") as f:
        json.dump(responses, f, indent=4)

# Function for replies
def chatbot_response(message):
    message = message.lower().strip()

    for key in responses:
        if key in message:
            return random.choice(responses[key])
    return "I don't understand. You can teach me by typing: add <question> = <answer>"

# Main loop
def run_chatbot():
    print("Bot: Hi! I'm your chatbot. Type 'bye' to exit.")

    while True:
        user_message = input("You: ").lower().strip()

        # Exit condition
        if user_message == "bye":
            print("Bot:", random.choice(responses["bye"]))
            save_responses()  # Save before exiting
            break

        # Add new reply dynamically
        if user_message.startswith("add "):
            try:
                parts = user_message[4:].split("=", 1)
                question = parts[0].strip().lower()
                answer = parts[1].strip()

                # Add new question or append to existing
                if question in responses:
                    responses[question].append(answer)
                else:
                    responses[question] = [answer]

                print(f"Bot: Got it! I'll remember that '{question}' can mean '{answer}'.")
                save_responses()  
            except:
                print("Bot: Oops! Use format: add question = answer")

        else:
            reply = chatbot_response(user_message)
            print("Bot:", reply)

# To Run chatbot

if __name__ == "__main__":
    run_chatbot()
