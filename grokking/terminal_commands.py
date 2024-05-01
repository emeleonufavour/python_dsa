import subprocess
import time
import speech_recognition as sr
import openai


def get_voice_input() -> str:
    """Function to get voice input from System Microphone

    Returns:
        str: result
    """
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Speak:")
        audio = recognizer.listen(source)
    try:
        command = recognizer.recognize_sphinx(audio)
        print("You said:", command)
        return command
    except sr.UnknownValueError:
        print("Could not understand audio")
        return ""
    except sr.RequestError as e:
        print(f"Could not request results; {e}")
        return ""


# OpenAI API key
api_key = ""
openai.api_key = api_key

# Define a list of commands
commands = [
    "say 'Good morning Tega, how can I help you today!'",
    # [
    #     "say Knock knock",
    #     "say Hello world!",
    #     "say NameError: name who is not defined"
    # ],
    # "say Stop being mean Favour",
    # "say Thank you, I will love that!"
]

# Execute each command in the list with a 3-second delay
for index, command in enumerate(commands):
    # Replace the command with voice input
    if (index == 0):
        subprocess.run(command, shell=True)
        time.sleep(3)
    else:
        if isinstance(command, list):
            for i in command:
                subprocess.run(i, shell=True)
                time.sleep(2)
        else:
            subprocess.run(command, shell=True)
            time.sleep(3)
