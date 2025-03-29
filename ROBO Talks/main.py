import os
import pyttsx3

engine = pyttsx3.init()
print("Welcome to ROBO-TALKS create by Yash")
while True:
    text = input("Enter what you want to speak: ")
    if text == "quit":

        text2 = "bye bye friend"
        engine.say(text2)
        engine.runAndWait()
        break
    engine.say(text)
    engine.runAndWait()