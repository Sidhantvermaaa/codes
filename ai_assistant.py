import speech_recognition as sr
import pyttsx3
import pywhatkit
import pyjokes
import spotify.sync as spotify  
import spotipy
import json
import webbrowser

username = '31aq6kdt3paiuas6hb3beqcrvdhu'
clientID = 'ca40685e53904cc0abba832c5cd62cfe'
clientSecret = 'd34e5dce201647b590e5beafedb8ceda'
redirect_uri = 'http://google.com/callback/'



listener = sr.Recognizer()
Jarvis = pyttsx3.init()
voices = Jarvis.getProperty('voices')
Jarvis.setProperty('voice', voices[1].id)


def speak(text):
    Jarvis.say(text)
    Jarvis.runAndWait()


def user_command():
    try:
        with sr.Microphone() as source:
            print('listening...')
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'jarvis' in command:
                command = command.replace('jarvis', '')
                print(command)
            

    except Exception as e:
        print(e)
        command = ''
    return command

##def message():
    try:
        with sr.Microphone() as source:
            speak('What is the message?')
            print('listening...')
            mssg = user_command
            speak('Which number do you want to send it to?')
            print('listening...')
            contact = user_command
            
            pywhatkit.sendwhatmsg(contact, mssg, 15, 5)
            print("Successfully sent!")

    except Exception as e:
        print(e)
        mssg = ''
    return mssg      


def run():
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
  ##  elif 'send' in command:
   ##     message()
    else:
        speak('Please say the command again.')


while True:
    run()