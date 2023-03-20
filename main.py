import pygame
import pyttsx3
import datetime
import wikipedia
import speech_recognition as sr
import webbrowser
import os

# Pygame Initializer
pygame.init()
screen_width = 500
screen_height = 400
white = [0,0,0]

gameWindow = pygame.display.set_mode((screen_width, screen_height))

bgimage = pygame.image.load("snake.jpg")
bgimage = pygame.transform.scale(bgimage, (screen_width, screen_height)).convert_alpha()

pygame.display.set_caption("Jarvis")
pygame.display.update()
font = pygame.font.SysFont(None, 55)

exit_game = False
game_over = False


# speak module initializer

browserPath = "C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s"
engine = pyttsx3.init('sapi5')   # TTS Engine for Windows
voices = engine.getProperty('voices')
# print(voices[1 ].id)
engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if 4 <= hour < 12:
        speak("Good Morning!")
    elif 12 <= hour < 16:
        speak("Good Afternoon!")
    elif 16 <= hour < 22:
        speak("Good Evening!")
    else:
        speak("Hello Master!")
    speak("I am Jarvis Sir. Please tell me how may I help you ")


def takeCommand():
    # It takes Voice input from user and returns string output
    r = sr.Recognizer()
    with sr.Microphone(device_index=1) as source:
        print("Listening.....")
        r.energy_threshold = 500
        r.pause_threshold = 0.5
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User Said: {query}\n")

    except Exception as e:
        print(e)
        print("Please repeat that again")
        return "None"
    return query


if __name__ == "__main__":
    while not exit_game:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit_game = True

            if event.type == pygame.KEYDOWN:
                wishMe()
                while (1):
                    query = takeCommand().lower()
                    # query = "Salman Khan wikipedia"
                    # logic for executing task based on query

                    if 'wikipedia' in query:
                        try:
                            speak("Searching Wikipedia...")
                            query = query.replace('wikipedia', "")
                            results = wikipedia.summary(query, sentences=2)
                            speak("According to wikipedia")
                            print(results)
                            speak(results)
                        except Exception as e:
                            print(e)
                            speak("Sorry, No results found on wikipedia. Can you please repeat that")

                    elif 'open youtube' in query:
                        speak("Opening youtube")
                        webbrowser.get(browserPath).open("https://www.youtube.com")

                    elif 'the time' in query:
                        strtime = datetime.datetime.now().strftime("%H:%M:%S")
                        speak(f"Sir, the time is {strtime}")

                    elif 'samay kya' in query:
                        strtime = datetime.datetime.now().strftime("%H:%M:%S")
                        speak(f"Sir, the time is {strtime}")

                    elif 'play music' in query:

                        musicdir = "D:\\music"
                        songs = os.listdir(musicdir)
                        print(songs)
                        speak("Playing music sir")
                        os.startfile(os.path.join(musicdir, songs[0]))

                    elif 'open code' in query:
                        codepath = "C:\\Users\\arjun\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
                        os.startfile(codepath)

                    elif ('quit' or 'jervis quit' or 'jarvis quit') in query:
                        speak("Quitting sir, have a nice day")
                        exit_game = True
                        break

                    elif 'hello jarvis' in query:
                        speak("Hello sir, how may I help you")

                    elif 'how are you' in query:
                        speak("I am very good sir how are you")

                    elif 'also good' in query:
                        speak("Wow that's great sir")

                    elif 'open google' in query:
                        speak("opening google")
                        webbrowser.get(browserPath).open("google.com")

                    elif 'open moodle' in query:
                        speak("opening moodle")
                        webbrowser.get(browserPath).open("http://lms.kiet.edu/moodle/")

                    elif 'bohemian rhapsody' in query:
                        speak("playing bohemian rhapsody")
                        songdir = "D:\\music\\bohemian rhapsody"
                        queen = os.listdir(songdir)
                        print(queen)
                        os.startfile(os.path.join(songdir, queen[0]))
            gameWindow.fill(white)
            gameWindow.blit(bgimage, (0, 0))
            pygame.display.update()
    pygame.quit()
    quit()