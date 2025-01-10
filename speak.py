# pip install pyttsx3

import pyttsx3
def speak(text):
    engine = pyttsx3.init()
    rate = engine.getProperty('rate')
    engine.setProperty('rate', rate-70)
    engine.say(text)
    engine.runAndWait()










# import pyttsx3

# def speak(text):
#     engine = pyttsx3.init()
#     voices = engine.getProperty('voices')  # Get the available voices
#     for voice in voices:
#         if "female" in voice.name.lower():  # Look for a female voice
#             engine.setProperty('voice', voice.id)  # Set the female voice
#             break
#     else:
#         engine.setProperty('voice', voices[0].id)  # Fallback to the first voice if no female voice found

#     rate = engine.getProperty('rate')
#     engine.setProperty('rate', rate - 70)  # Adjust the speech rate
#     engine.say(text)
#     engine.runAndWait()
