import datetime
import os
import time
import webbrowser

import cv2
import pyautogui
import pyjokes
import pyttsx3
import pywhatkit
import speech_recognition as sr

engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
voice_rate = 150
engine.setProperty("rate", voice_rate)
engine.setProperty("voice", voices[0].id)  # 1- Zira,Female  0-David,male

# Create a function
def speak(audio):
    engine.say(audio)
    print(audio)
    engine.runAndWait()


def take_command():
    r = sr.Recognizer()
    mic = sr.Microphone()
    with mic as source:
        print("Please wait. Calibrating microphone...")
        r.adjust_for_ambient_noise(source, duration=3)
        print("Listening...")
        audio = r.listen(source)
    try:
        print("Recognition...")
        print(r.recognize_google(audio, language="en-GB"))
        return
    except sr.UnknownValueError:
        speak("Say that again please...")
        take_command()


def initialing():
    print("Initialing...")
    time.sleep(5)
    hour = datetime.datetime.now().hour
    if 0 <= int(hour) < 12:
        speak("Good morning sir!")
    elif 12 <= int(hour) < 18:
        speak("Good afternoon sir!")
    else:
        speak("Good evening sir!")
    speak("I am jarvis sir, please tell me how can i help you?")


def date_and_time():
    hour = datetime.datetime.now()
    speak(hour.strftime("Today is %x and the clock is %H:%M %p"))


def command_application():
    r = sr.Recognizer()
    mic = sr.Microphone()
    with mic as source:
        print("Please wait. Calibrating microphone...")
        r.adjust_for_ambient_noise(source, duration=3)
        print("Listening...")
        audio = r.listen(source)
    try:
        print("Recognition...")
        command = r.recognize_google(audio, language="en-GB")
        print(command)
    except sr.UnknownValueError:
        speak("Say that again please...")
        command_application()
    command = command.lower()

    # logic building for tasks

    # open the Command prompt
    if "open command" in command:
        os.system("start cmd")

    # switch between open windows
    if "switch the window" in command:
        with pyautogui.hold('alt'):
            pyautogui.press('tab')

    # open task manager
    if "manager" in command:
        pyautogui.hotkey('ctrl', 'shift', 'esc')

    # take a screenshot
    if "screenshot" in command:
        pyautogui.hotkey('win', 'alt', 'prtscr')

    # open youtube in browser
    if "open youtube" in command:
        webbrowser.open("https://www.youtube.com/")

    # open facebook in browser
    if "open facebook" in command:
        webbrowser.open("https://www.facebook.com/")

    # play music on youtube
    if "play music" in command:
        pywhatkit.playonyt("blinding lights")

    # send messages via WhatsApp
    if "message" in command:
        pywhatkit.sendwhatmsg("+40748806465", "Frate langa frate", 12, 58, 15, True, 2)

    # search on Google about something
    if "open google" in command:
        speak("Sir,what should i search on google")
        with mic as source:
            print("Please wait. Calibrating microphone...")
            r.adjust_for_ambient_noise(source, duration=3)
            print("Listening...")
            audio = r.listen(source)
        command = r.recognize_google(audio, language="en-GB")
        webbrowser.open(f"{command}")

    # open camera
    if "open camera" in command:
        video = cv2.VideoCapture(0)
        while True:
            ret, img = video.read()
            cv2.imshow('webcam', img)
            if cv2.waitKey(0) & 0xFF == ord('x'):
                break
        video.release()
        cv2.destroyAllWindows()

    # jarvis tell you a joke
    if "tell me a joke" in command:
        joke = pyjokes.get_joke()
        speak(joke)

    # jarvis tell you date and time at the present moment
    if "date and time" in command:
        date_and_time()

    # shutdown the laptop
    if "shutdown" in command:
        os.system("shutdown /s /t 2")

    # restart the laptop
    if "restart" in command:
        os.system("shutdown /r /t 2")

    # log off the laptop
    if "log off" in command:
        os.system("shutdown -l")

    # close jarvis
    if "you can sleep " in command:
        speak("thanks for using me sir, have a good day.")
        return


    speak("sir, do you have any other work?")
    command_application()


initialing()
command_application()
