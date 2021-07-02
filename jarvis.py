import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import smtplib
import webbrowser as wb
import os
import pyautogui
import psutil
import pyjokes




engine=pyttsx3.init()
# voices=engine.getProperty('voices')
# engine.setProperty('voice',voices[0].id)
# newVoicesRate=120
# engine.setProperty('rate',newVoicesRate)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def time():
    Time=datetime.datetime.now().strftime("%I:%M:%S")
    speak(Time)

def date():
    year=int(datetime.datetime.now().year)
    month=int(datetime.datetime.now().month)
    date=int(datetime.datetime.now().day)
    speak("The Current Date is")
    speak(date)
    speak(month)
    speak(year)

def wishme():
    speak("Welcome back mam!")

    hour=datetime.datetime.now().hour

    if hour > 6 and hour <= 12:
        speak("Good Morning")
    elif hour >= 12 and hour < 18:
        speak("Good Afternoon")
    elif hour >= 18 and hour <= 24:
        speak("Good Evening")
    else:
        speak("Good Night")

    speak("Dorla at your service.How i can help you?")



def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening....")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio,language='en=US')
        print(query)
    except Exception as e:
        print(e)
        speak("Say that again please...")

        return "None"

    return query

# def sendmail(to, content):
#     server=smtplib.SMTP('smtp.gmail.com',587)
#     server.ehlo()
#     server.starttls()
#     server.login("anusuyathyagaraj20@gmail.com","namitha$321")
#     server.sendmail("anusuyathyagaraj20@gmail.com",to, content)
#     server.close()

def screenshot():
    img=pyautogui.screenshot()
    img.save("F:\Jarvis Images\img.png")

def cpu():
    usage = str(psutil.cpu_percent())
    speak("CPU is at " + usage)

    battery= psutil.sensors_battery()
    speak("Battery is at")
    speak(battery.percent)
    speak("Battery is plugged")
    speak(battery.power_plugged)

def joke():
    speak(pyjokes.get_joke())


if __name__== "__main__":

    wishme()

    while True:
        query = takeCommand().lower()
        print(query)

        if "time" in query:
            time()

        elif "date" in query:
            date()

        elif "offline" in query:
            quit()

        elif "wikipedia" in query:
            speak("Searching...")
            query = query.replace("wikipedia", "")
            result = wikipedia.summary(query, sentences = 2)
            speak(result)

        # elif "send email" in query:
        #     try:
        #         speak("What should i say?")
        #         content = takeCommand()
        #         to="anusuyathyagaraj20@gmail.com"
        #         #sendmail(to, content)
        #         speak("Email was sent succesfully")
        #     except Exception as e:
        #         speak(e)
        #         speak("Unable to send the mail")

        elif "search in chrome" in query :
            speak("what should i search?")
            chromepath = "C:\Program Files\Google\Chrome\Application\chrome.exe %s"
            search = takeCommand().lower()
            wb.get(chromepath).open_new_tab(search+ ".com")

        elif "logout" in query:
            os.system("shutdown - l")

        elif "shutdown" in query:
            os.system("shutdown /s /t 1")

        elif "restart" in query:
            os.system("shutdown /r /t 1")

        elif "play songs" in query:
            songs_dir="F:\Music"
            songs=os.listdir(songs_dir)
            os.startfile(os.path.join(songs_dir, songs[0]))

        elif "remember" in query:
            speak("what should i remember?")
            data=takeCommand()
            speak("you said me to remember" + data)
            remember = open("data.txt","w")
            remember.write(data)
            remember.close()

        elif "do you know anything" in query:
            remember = open("data.txt","r")
            speak("you said me to remember that " + remember.read())

        elif "screenshot" in query:
            screenshot()
            speak("Done")

        elif "cpu" in query:
            cpu()

        elif "joke" in query:
            joke()

