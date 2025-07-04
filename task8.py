print("Hi! I'm ChatSimple. Type 'bye' to exit.")

while True:
    user_input = input("You: ").lower()

    if "hello" in user_input or "hi" in user_input:
        print("ChatSimple: Hey there! How can I help you?")
    elif "how are you" in user_input:
        print("ChatSimple: I'm just a bunch of Python code, but I'm doing great!")
    elif "your name" in user_input:
        print("ChatSimple: I'm ChatSimple, your rule-based chatbot.")
    elif "weather" in user_input:
        print("ChatSimple: I'm not connected to the internet, but it's always sunny in my terminal!")
    elif "bye" in user_input:
        print("ChatSimple: Goodbye! Have a great day.")
        break
    else:
        print("ChatSimple: I'm still learning... Can you try asking something else?")