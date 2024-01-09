def show_messages(messages):
    for message in messages:
        print(message)
# Creating a list of short text messages
text_messages = [
    "Hello!",
    "How are you?",
    "Python is fun!",
    "Learning programming",
    "Have a great day!"
]

# Calling the show_messages() function to print each text message
show_messages(text_messages)
def send_messages(messages, sent_messages):
    while messages:
        current_message = messages.pop(0)
        print(f"Sending message: {current_message}")
        sent_messages.append(current_message)

# Creating a list of short text messages
text_messages = [
    "Hello!",
    "How are you?",
    "Python is fun!",
    "Learning programming",
    "Have a great day!"
]

# Creating an empty list to store sent messages
sent_messages = []

# Calling the send_messages() function to print and move messages
send_messages(text_messages, sent_messages)

# Printing both lists to verify the messages were moved correctly
print("Original Messages:", text_messages)
print("Sent Messages:", sent_messages)
def make_sandwich(*items):
    print("Making a sandwich with the following items:")
    for item in items:
        print(f"- {item}")
    print("Enjoy your sandwich!\n")

# Calling the function with different numbers of arguments
make_sandwich("Turkey", "Cheese", "Lettuce", "Tomato")
make_sandwich("Ham", "Swiss Cheese", "Mustard")
make_sandwich("Peanut Butter", "Jelly")