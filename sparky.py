
from ai import AI
# Import TTS & SR AI

sparky = AI()
# Define an instance of AI

command = ""

while True and command != "shutdown":
    try:
        command = sparky.listen()
        # Tell AI to listen for command
        command = command.lower()
    except:
        print("I couldn't catch that.")
        command = ""

    print("command: " + command)
        
