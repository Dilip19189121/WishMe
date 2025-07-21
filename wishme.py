import pyttsx3
import datetime

def get_greeting():
    hour = datetime.datetime.now().hour
    if hour < 12:
        return "Good morning, Sir! Hope you slept well."
    elif hour < 17:
        return "Good afternoon, Sir! Ready to keep the momentum going?"
    elif hour < 21:
        return "Good evening, Sir! Let’s wind down with purpose."
    else:
        return "Hello, Sir! Burning the midnight oil again?"

# Initialize the voice engine
engine = pyttsx3.init()

# Generate the time-based greeting
greeting = get_greeting()

# Speak it aloud
engine.say(greeting)
engine.runAndWait()

# Print it to the terminal for confirmation
print(greeting)