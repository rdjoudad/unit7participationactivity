prompt = "If you share your name, we can personalize the messages you see."
prompt += "\n What is your first name? "

message = ''
while message != 'quit':
    message = input(prompt)
    if message != 'quit':
        print(message)
