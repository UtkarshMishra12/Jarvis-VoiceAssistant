import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import smtplib


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voices', voices[0].id)



def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")
    
    elif hour>12 and hour<18:
        speak("Good Afternoon!")

    else:
        speak("Good Evening!")    

    speak("I am Jarvis Sir , Please tell me how may I help you")

def takeCommand():
    #it take microphone input from the user and returns string command
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening.....")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')  
        print(f" User said: {query}\n") 


    except Exception as e:
        #print(e) 

        print("Say that again Please...")
        return "None"   
    return query

def sendEmail(to , content):
    server = smtplib.SMTP('smtp.gmail.com', 587) 
    server.ehlo()
    server.starttls()
    server.login("youremail@gmail.com", 'your-password')
    server.sendmail('youremail@gmail.com', to, content)
    server.close()


if __name__ == "__main__":
    wishMe()
    while True:
    #if 1:
        query = takeCommand().lower()

        #logic for executing task
        if 'wikipedia' in query:
            speak('Searching Wikipedia')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=1)
            speak("Acording to Wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open('youtube.com')

        elif 'open google' in query:
            webbrowser.open('google.com')  

        elif 'open stackoverflow' in query:
            webbrowser.open('stackoverflow.com')    

        elif 'play music' in query:
            music_dir = 'C:\\Music' 
            songs = os.listdir(music_dir)  
            os.startfile(os.path.join(music_dir, songs[0]))

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")   
            print(strTime) 
            speak(f"Sir the Time is {strTime}")

        elif 'open code' in query:
            codePath = "C:\\Users\\hp\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"    
            os.startfile(codePath)

        elif 'send email' in query:
            try:
                speak("What should I say")
                content = takeCommand()
                to = "194@gmail.com"
                sendEmail(to, content)
                speak("Email has been sent")
            except Exception as e:
                print(e)
                speak("Sorry my friend utkarsh, i am unable to send the email")    

        elif 'exit' in query:
            speak("Thank you utkarsh see you soon!")
            exit()        

        elif 'how are you' in query:
            speak("I am good sir ,what about you")

        elif 'open facebook' in query:
            webbrowser.open('facebook.com')

        elif 'created' in query:
            speak('I am created by Utkarsh Mishra')            