prompt = "\nTell me something and I will repeat it back to you:"
prompt += "\nEnter 'quit' to end the program. "


while True:
    message = input(prompt)
    if message == 'quit':
        break
    elif message == 'parrot':
        print("Oh, you think you're a wise guy, huh?")
        break
    else:
        print(message)
