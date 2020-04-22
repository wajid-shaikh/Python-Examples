import pyttsx3 #pip install pyttsx3
import speech_recognition as sr #pip install speechRecognition
import datetime
import wikipedia #pip install wikipedia
import webbrowser
import os
import smtplib
# pocket sphinx
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice', voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")
    elif hour>=12 and hour<18:
        speak("Good Afternoon!")   
    else:
        speak("Good Evening!")  

    speak("I am Jarvis Sir. Please tell me how may I help you")       

def takeCommand():
    #It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        # print(e)    
        print("Say that again please...")  
        return "None"
    return query

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('youremail@gmail.com', 'your-password')
    server.sendmail('youremail@gmail.com', to, content)
    server.close()

if __name__ == "__main__":
    wishMe()
    while True:
    # if 1:
        query = takeCommand().lower()

        # Logic for executing tasks based on query
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")   

        elif 'play music alone' in query:
            music_dir = 'C:\\Users\\Wajid Shaikh\\Desktop\\hollywood songs\\'
            songs = os.listdir(music_dir)
            print(songs)    
            os.startfile(os.path.join(music_dir, songs[6]))

        elif 'play music darkside' in query:
            music_dir = 'C:\\Users\\Wajid Shaikh\\Desktop\\hollywood songs\\'
            songs = os.listdir(music_dir)
            print(songs)    
            os.startfile(os.path.join(music_dir, songs[23]))

        elif 'play music different world' in query:
            music_dir = 'C:\\Users\\Wajid Shaikh\\Desktop\\hollywood songs\\'
            songs = os.listdir(music_dir)
            print(songs)    
            os.startfile(os.path.join(music_dir, songs[25]))

        elif 'play music alan walker' in query:
            music_dir = 'C:\\Users\\Wajid Shaikh\\Desktop\\hollywood songs\\'
            songs = os.listdir(music_dir)
            print(songs)    
            os.startfile(os.path.join(music_dir, songs[69]))

        elif 'play music abcd' in query:
            music_dir = 'C:\\Users\\Wajid Shaikh\\Desktop\\bollywood music\\'
            songs = os.listdir(music_dir)
            print(songs)    
            os.startfile(os.path.join(music_dir, songs[54]))

        elif 'play music maula mere maula' in query:
            music_dir = 'C:\\Users\\Wajid Shaikh\\Desktop\\bollywood music\\'
            songs = os.listdir(music_dir)
            print(songs)    
            os.startfile(os.path.join(music_dir, songs[87]))

        elif 'play music cocktail' in query:
            music_dir = 'C:\\Users\\Wajid Shaikh\\Desktop\\bollywood music\\'
            songs = os.listdir(music_dir)
            print(songs)    
            os.startfile(os.path.join(music_dir, songs[0]))

        # elif 'play movie alan walker' in query:
        #     movie_dir = 'C:\\Users\\Wajid Shaikh\\Desktop\\bollywood movie\\'
        #     movies = os.listdir(movie_dir)
        #     print(movies)    
        #     os.startfile(os.path.join(movie_dir, movies[69]))

        elif 'play movie avengers endgame' in query:
            movie_dir = 'F:\\movies\\Hollywood\\'
            movies = os.listdir(movie_dir)
            print(movies)    
            os.startfile(os.path.join(movie_dir, movies[24]))

        elif 'play movie guardians of galaxy' in query:
            movie_dir = 'F:\\movies\\Hollywood\\'
            movies = os.listdir(movie_dir)
            print(movies)    
            os.startfile(os.path.join(movie_dir, movies[66]))

        elif 'play movie tanhaji' in query:
            movie_dir = 'E:\\Bollywood\\'
            movies = os.listdir(movie_dir)
            print(movies)    
            os.startfile(os.path.join(movie_dir, movies[22]))

        elif 'play movie kungfu panda' in query:
            movie_dir = 'E:\Animation\\'
            movies = os.listdir(movie_dir)
            print(movies)    
            os.startfile(os.path.join(movie_dir, movies[20]))




        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            speak(f"Sir, the time is {strTime}")

        elif 'open code' in query:
            codePath = "C:\\Users\\Haris\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)

        elif 'email to harry' in query:
            try:
                speak("What should I say?")
                content = takeCommand()
                to = "harryyourEmail@gmail.com"    
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry my friend harry bhai. I am not able to send this email")    
