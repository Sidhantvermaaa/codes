import speech_recognition as sr
import pyttsx3
import pywhatkit
import pyjokes
import datetime
import wikipedia
from requests import get

listener = sr.Recognizer()
Jarvis = pyttsx3.init()
voices = Jarvis.getProperty('voices')
rate = Jarvis.getProperty('rate')
Jarvis.setProperty('rate', rate-10)
Jarvis.setProperty('voice', 'com.apple.eloquence.en-US.Daniel')


def speak(text):
    Jarvis.say(text)
    print(text)
    Jarvis.runAndWait()


def user_command():
    try:
        with sr.Microphone() as source:
            print('listening...')
            listener.pause_threshold= 1
            voice = listener.listen(source, timeout=1,phrase_time_limit=5)
            command = listener.recognize_google(voice, language='en-in')
            command = command.lower()
            if 'jarvis' in command:
                command = command.replace('jarvis', '')
                print(command)
            

    except Exception as e:
        print(e)
        command = ''
    return command

def wish():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<=12:
        speak('good morning ')
    elif hour>12 and hour<18:
        speak('good afternoon')
    else:
        speak('good evening')
    speak('Hi I am Jarvis, what would you like me to do for you today?')

def run():
    wish()
    command = user_command()
    print(command)
    if 'alexa' in command:
        speak('Who the hell is Alexa?')
    elif 'siri' in command:
        speak('Who the hell is Siri?')
    elif 'google' in command:
        speak('Who the hell is Google?')
    elif 'Hi Jarvis' in command:
        speak('Hi human!')
    elif 'play' in command:
        song = command.replace('play', '')
        speak('playing' + song)
        pywhatkit.playonyt(song)
    elif 'joke' in command:
        command_joke = pyjokes.get_joke()
        speak('Here\'s a good joke.. ' '   '+ command_joke)
        print(command_joke)
    elif 'ip address' in command:
        ip = get('https://api.ipify.org').text
        speak(f'Your IP address is {ip}')
    elif 'what is' in command:
        speak('searching wikipedia...')
        command = command.replace('what is', '')
        results = wikipedia.summary(command, sentences = 2)
        speak('according to wikipedia')
        speak(results)
    elif 'send message' in command:
        msg = command.replace('send message', '')
        pywhatkit.sendwhatmsg('+919354142443', msg,00,46)
        speak('it will be done')

    else:
        speak('Please say the command again.')


while True:
    run()