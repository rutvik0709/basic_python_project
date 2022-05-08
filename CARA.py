import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import smtplib
import imdb
import wolframalpha
import pyautogui

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning!")

    elif hour >= 12 and hour < 17:
        speak("Good Afternoon!")

    else:
        speak("Good Evening!")

    speak("I am Cara Sir. Please tell me how may I help you")


def listen():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Say Something!")
        audio = r.listen(source, phrase_time_limit=5)
        print("Recognizing...")
    try:
        query = r.recognize_google(audio)
        print("you said: " + query)
        # return query
    except sr.UnknownValueError:
        print("Could not understand the audio, Please try again")
        return "None"
    return query


def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('rutvik.manchekar20@vit.edu', '12010592')
    server.sendmail('rutvik.manchekar20@vit.edu', to, content)
    server.close()


def imdbpy(x):
    global y
    moviesdb = imdb.IMDb()
    search = x
    # os.start
    movies = moviesdb.search_movie(search)

    print("Searching for " + search)
    if len(movies) == 0:
        y = "No movies found."
    else:
        for movie in movies:
            title = movie['title']
            year = movie['year']
            print(f"{title} {year}")

            info = movie.getID()
            movie = moviesdb.get_movie(info)

            title = movie['title']
            year = movie['year']

            if year < int(datetime.datetime.now().strftime("%Y")):
                rating = movie['rating']
                y = "{title} was released in {year} has IMDb rating of {rating}."
                break
            else:
                y = "{title} will release in {year}. As it is yet to release it has no rating."
                break

    return y


def wolframaplha(question):
    client = wolframalpha.Client('YKXG5E-HQKX6GUH22')
    res = client.query(question)
    answer = next(res.results).text
    return answer


def screenshots():
    Screenshot = pyautogui.screenshot()
    speak('What name do u want to keep.')
    a = listen().lower()
    Screenshot.save(f'D:\\{a}.jpeg')
    os.startfile(f'D:\\{a}.jpeg')
    speak('Your screenshot has been saved.')


# if __name__ == '__main__':
def main():
    wishMe()
    while True:
        query = listen().lower()

        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            speak("What do u want to watch?")
            a = listen().lower()
            webbrowser.open("https://www.youtube.com/results?search_query={0}".format(a))

        elif 'open google' in query:

            speak("What do u want to search?")
            a = listen().lower()
            webbrowser.open("https://www.google.com/search?client=firefox-b-d&q={0}".format(a))

        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")

        elif 'play music' in query:
            music_dir = 'D:\\song1'
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir, songs[0]))

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the time is {strTime}")

        elif "who are you" in query or "define yourself" in query:
            say = "Hello, I am Cara. Your personal Assistant. I am here to make your life easier. You can command " \
                  "me to perform various tasks such as calculating sums or opening applications etcetra "
            speak(say)

        elif "who made you" in query or "created you" in query:
            say = "I have been created by Aryan, Rutvik, Ram, Harsha and Digvijay"
            speak(say)

        elif "calculate" in query.lower():
            speak("What do you want to calculate?")
            calc = listen()
            say = wolframaplha(calc)
            speak(say)

        elif "movie" in query.lower():
            speak("Which movie do you want to search?")
            movie = listen()
            say = imdbpy(movie)
            speak(say)

        elif 'please email' in query:
            try:
                speak("What should I say?")
                content = listen()
                to = "rutvik0709@gmail.com"
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry,not able to send this email")

        elif 'take screenshot' in query:
            screenshots()

        elif 'goodbye' in query:
            hour = int(datetime.datetime.now().hour)
            if hour >= 6 and hour < 20:
                speak("GoodBye Sir")
            else:
                speak("Good Night sir")

            exit(0)


main()