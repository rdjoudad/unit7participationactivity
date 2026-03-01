prompt = "\nTell me something and I will repeat it back to you:"
prompt += "\nEnter 'quit' to end the program. "

active = True
while active:
    message = input(prompt)
    if message == 'quit':
        active = False
    elif message == 'parrot':
        active = False
        print("Oh, you think you're a wise guy, huh?")
    else:
        print(message)
