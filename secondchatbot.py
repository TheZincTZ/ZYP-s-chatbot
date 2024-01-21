# Import the necessary library
import time

# Define a function for the chatbot to greet the user
def greet():
    print("Hello! I'm TheZinc's chatbot. This is a chatbot made for her. If you are her, you will get access to the whole chatbot.")

# Define a function for the chatbot to listen for the keyword "Zi Ying"
def listen_for_keyword():
    user_input = input("You: ")
    if "zi ying" in user_input.lower():
        print("Chatbot: Full access granted.")
        return "full_access"
    else:
        return user_input

# Define a function for the chatbot to listen for general user input
# Define a function for the chatbot to listen for general user input
def listen_for_chat():
    print("Chatbot: What would you like to do?")
    print("1. Contact Zinc here")
    print("2. Information about Zinc")
    print("3. Play a game")
    print("4. Message from Zinc")
    print("5. Exit")
    while True:
        user_input = input("You: ")
        if user_input in ["1", "2", "3", "4"]:
            return user_input
        elif user_input == "5":
            print("You have exited the programme")
            return False
            
        else:
            print("Chatbot: Invalid choice. Please enter a number from 1 to 4.")


# Main function to run the chatbot
def main():
    greet()
    while True:
        user_input = listen_for_keyword()
        key = True
        if user_input == "full_access":
            # Add your logic here to provide full access to the chatbot
            print("Chatbot: Welcome, Zi Ying! You now have full access.")
            # Add your logic here to chat with Zi Ying
            while key:
                listen_for_chat()
        else:
            # Add your logic here to respond to the user input
            print("ChatBot: Full access is not granted as you are not the correct user")

# Run the main function
if __name__ == "__main__":
    main()
