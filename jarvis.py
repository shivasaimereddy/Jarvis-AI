from email import encoders
import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
from pywikihow import WikiHow, search_wikihow
import webbrowser
import os
import smtplib
import random
import requests
import pyautogui
from pyautogui import keyDown
from pyautogui import keyUp
from pyautogui import press
import pywhatkit as kit
import time
import email
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email.encoders import encode_base64
import instaloader
import PyPDF2
import getpass
import psutil
from youtube import youtube
from weather import weather
from dictionary import translate
from news import speak_news, getNewsUrl
import speedtest
import speedtest_cli
import twilio
from twilio.rest import Client


webbrowser.register('chrome',
                    None,
                    webbrowser.BackgroundBrowser("C:\Program Files (x86)\Google\Chrome\Application\chrome.exe"))


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


MASTER = "master"


def takeCommand():

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Jarvis: Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize(audio)
        print(f"{MASTER}: {query}\n")

    except Exception as e:
        print(e)
        print("Say that again please...")
        return "None"
    return query


def sendMSG():
    speak('what should i say')
    msg = input("Enter Message:")

    account_sid = ''
    auth_token = ''

    client = Client(account_sid, auth_token)

    message = client.messages\
        .create(
            body=msg,
            from_='',
            to=''
        )

    print(message.sid)


def cpu():
    usage = str(psutil.cpu_percent())
    speak("CPU usage is at"+usage)

    battery = psutil.sensors_battery()
    speak("Laptops battery is at")
    speak(battery.percent + "percent")


def pdf_reader():
    try:

        book = open('', 'rb')
        pdfReader = PyPDF2.PdfFileReader(book)
        pages = pdfReader.numPages
        speak(f"total number of pages in this pdf is {pages}")
        speak("enter the page number you wish to listen")
        pg = int(input("Enter Page Number: "))
        page = pdfReader.getPage(pg)
        text = page.extractText()
        speak(text)

    except Exception as e:
        print(e)


def commands():
    while True:
        query = takeCommand().lower()

        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif "cpu" in query or "cpu details" in query:
            cpu()

        elif 'dictionary' in query:
            speak('What you want to search in your dictionary?')
            translate(takeCommand())

        elif 'news' in query:
            speak('okay..')
            speak_news()
            speak('Do you want to read the full news...')
            test = takeCommand()
            if 'yes' in test:
                speak('Ok Sir, Opening browser...')
                webbrowser.open(getNewsUrl())
                speak('You can now read the full news from this website.')

        elif 'open youtube' in query:
            webbrowser.get('chrome').open("youtube.com")

        elif 'search youtube' in query:
            speak('What you want to search on Youtube?')
            youtube(takeCommand())

        elif 'search internet' in query:
            speak("what should i search on internet")
            cm = takeCommand().lower()
            webbrowser.open(f'{cm}')

        elif 'stackoverflow' in query:
            webbrowser.get('chrome').open("stackoverflow.com")

        elif 'github' in query:
            webbrowser.get('chrome').open("https://github.com/shivasaimereddy")

        elif 'music' in query:
            music_dir = 'enter music path'
            songs = os.listdir(music_dir)
            rd = random.choice(songs)
            print(songs)
            for song in songs:
                if song.endswith('.mp3'):
                    os.startfile(os.path.join(music_dir, rd))

        elif 'search for a location' in query or "location" in query:
            speak('What is the location?')
            location = takeCommand()
            url = 'https://google.nl/maps/place/' + location + '/&amp;'
            webbrowser.get('chrome').open_new_tab(url)
            speak('Here is the location ' + location)

        elif 'remember this' in query or 'remember' in query:
            speak("Ok, tell me")
            rememberMessage = takeCommand()
            speak("you said me "+rememberMessage)
            remember = open('note.txt', 'w')
            remember.write(rememberMessage)
            remember.close()

        elif 'did you remember anything' in query or 'read data' in query:
            remember = open('note.txt', 'r')
            speak("you said me to remember that" + remember.read())

        elif 'switch to friday' in query:
            engine.setProperty('voice', voices[1].id)
            speak("Hello Sir, I am friday. How may i assist you")

        elif 'switch to jarvis' in query:
            engine.setProperty('voice', voices[0].id)
            speak("Hello Sir, Jarvis is back. How may i assist you?")

        elif "stop" in query:
            speak("ok")
            os.system("taskkill /f /ai music")

        elif 'time' in query:
            strTime = datetime.datetime.now().strftime("%I:%M")
            speak(f"Sir, the time is {strTime}")

        elif "play song on youtube" in query:
            kit.playonyt("salt")

        elif 'open code' in query:
            codePath = "code.exe path"
            os.startfile(codePath)

        elif 'close code' in query:
            speak("Closing Code")
            os.system("taskkill /f /im code.exe")

        elif "ip address" in query:
            ip = requests.get('https://api.ipify.org').text
            speak(f"your ip address is {ip}")

        elif "where am i" in query:
            speak("You have not programmed me that well, ok... let me try ")
            try:
                ipAdd = requests.get('https://api.ipify.org').text
                print(ipAdd)
                url = 'https://get.geojs.io/v1/ip/geo/'+ipAdd+'.json'
                geo_requests = requests.get(url)
                geo_data = geo_requests.json()
                city = geo_data['city']
                country = geo_data['Country']
                speak(f'we are in {city} of {country}')
            except Exception as e:
                print(e)
                speak("its difficult for me")
                speak("I already told you, you have not programmed me that good.")

        elif "switch desktop" in query:
            keyDown("alt")
            press("tab")
            keyUp("alt")

        elif "open notepad" in query:
            npath = "C:\\WINDOWS\\system32\\notepad.exe"
            os.startfile(npath)

        elif "close notepad" in query:
            speak("Closing Notepad")
            os.system("taskkill /f /im notepad.exe")

        elif "open command prompt" in query:
            os.system("start cmd")

        elif ("shutdown system") in query:
            speak("Do you want me to turn off laptop")
            takeCommand()
            if "yes" in query:
                os.system("shutdown /s /t 5")
            else:
                speak("cool, im not doing that")
                speak("im listening")
                takeCommand()

        elif "restart system" in query:
            os.system("shitdown /r /t 5")

        elif "sleep" in query:
            os.system("rundll32.exe powrprof.dll, SetSuspendState 0,1,0")

        elif "send email" in query or "send mail" in query:
            email = ""
            password = ""
            speak("enter the email address of the recipient")
            recipient = input("Enter Email Address: ")
            speak("What is the subject of the mail")
            query = takeCommand().lower()
            subject = query
            speak("and what is the message")
            query2 = takeCommand().lower()
            message = query2
            speak("Do you want to attach any file")
            query3 = takeCommand().lower()
            if "yes" in query3:
                speak("Ok, i can help you with that")
                speak("enter the correct path of file into the shell")
                file_location = input("Enter path")
                speak("please wait, im sending the email now")

                msg = MIMEMultipart()
                msg['From'] = email
                msg['To'] = recipient
                msg['Subject'] = subject

                msg.attach(MIMEText(message, 'plain'))

                filename = os.path.basename(file_location)
                attachment = open(file_location, 'rb')
                part = MIMEBase('application', 'octet-stream')
                part.set_payload(attachment.read())
                encoders.encode_base64(part)
                part.add_header('Content-Disposition',
                                "attachment; filename= %s" % filename)

                msg.attach(part)

                server = smtplib.SMTP('smtp.gmail.com', 587)
                server.starttls()
                server.login(email, password)
                text = msg.as_string()
                server.sendmail(email, recipient, text)
                server.quit()
                speak("email has been sent")
            else:
                speak("please wait, im sending email now")
                msg = MIMEMultipart()
                msg['From'] = email
                msg['To'] = recipient
                msg['Subject'] = subject

                msg.attach(MIMEText(message, 'plain'))

                server = smtplib.SMTP('smtp.gmail.com', 587)
                server.starttls()
                server.login(email, password)
                text = msg.as_string()
                server.sendmail(email, recipient, text)
                server.quit()
                speak("email has been sent")

        elif 'send message' in query or 'message' in query:
            speak('what should i say')
            msg = takeCommand()

            account_sid = ''
            auth_token = ''

            client = Client(account_sid, auth_token)

            message = client.message\
                .create(
                    body=msg,
                    from_='',
                    to=''
                )

            print(message.sid)

        elif "whats app" in query:
            kit.sendwhatmsg("enter number", "Jarvis test message", 2, 25)

        elif "screenshot" in query:
            speak("suggest a name for screenshot")
            name = takeCommand().lower()
            speak("Ok, just a second")
            img = pyautogui.screenshot()
            img.save(f"{name}.png")
            speak("Screenshot saved in mainframe, Job Done")

        elif "instagram" in query or "instagram profile" in query:
            speak("enter username")
            name = input("enter username")
            webbrowser.open(f"www.instagram.com/{name}")
            speak(f"here is the profile of {name}")
            time.sleep(3)
            speak("do you want to download this profic picture")
            condition = takeCommand().lower()
            if "yes" in condition or "yeah" in condition:

                try:
                    mod = instaloader.Instaloader()
                    mod.download_profile(name.get(), profile_pic_only=True)
                    speak("Done, image stored in main frame")
                except Exception as e:
                    print(e)

            else:
                speak("I cant do that at the moment")

        elif "read" in query or "read pdf" in query:
            pdf_reader()

        elif "folder actions" in query or "folder" in query or "this folder" in query:
            speak("what action do you want to perform")
            condition = takeCommand().lower()
            if "hide" in condition or "hide all files" in condition:
                os.system("attrib +h /s /d")
                speak("all the files are now hidden")

            elif "visible" in condition or "make all files visible" in condition:
                os.system("attrib -h /s /d")
                speak("all files are now visible")

            elif "leave for now" in condition:
                speak("cool")

        elif "hide all files" in query:
            os.system("attrib +h /s /d")
            speak("all the files are now hidden")

        elif "make all files visible" in query:
            os.system("attrib -h /s /d")
            speak("all files are now visible")

        elif 'jarvis are you there' in query:
            speak('yes sir, at your service')

        elif 'who are you' in query:
            speak('im jarvis, Just A Rather Very Intelligent System. i can perform some basic desktop actions that can make your work simple')

        elif 'what can you do' in query:
            speak('ask me something, you will get to know, what i can do.')

        elif 'internet speed' in query or 'check internet speed' in query:
            st = speedtest.Speedtest()
            dl = st.download()
            up = st.upload()
            speak(
                f'we have {dl} bits per second download speed and {up} bits per second upload speed')

        elif 'see you later' in query or 'bye' in query:
            speak("Im signing off, have a good day")
            exit()


def takeAuth():

    r = sr.Recognizer()
    with sr.Microphone() as source:
        speak("Hi, im Jarvis. Confirm Your Identity")
        print("Confirm Your Identity")
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize(audio)
        print(f"Identity: {query}\n")
        if MASTER in query:
            speak(f"Hi {MASTER}, Enter your Access Key")
            pin = int(input("Enter Access Key: "))

            if(pin == 123):
                speak(
                    "Access Granted, Welcome Back sir. All systems are now initiated and running.")
                start()
                commands()
            else:
                speak(f"Incorrect Access Key, {MASTER}. Please retry")
                pin = int(input("Enter Access Key: "))
                if(pin == 123):
                    speak("Access Granted")
                    start()
                    commands()
                else:
                    speak("Incorrect Access Key, last chance to retry")
                    pin = int(input("Enter Access Key: "))
                    if(pin == 123):
                        speak("Access Granted")
                        start()
                        commands()
                    else:
                        speak("Sorry, Incorrect Key. Im shutting down!")
                        exit()

        else:
            speak("you are not an authorized master, im shutting down.")
            exit()

    except Exception as e:
        print(e)
        speak("Error, im shutting down")
        return "None"


def start():
    hour = int(datetime.datetime.now().hour)
    strTime = datetime.datetime.now().strftime("%I:%M")
    if hour >= 0 and hour < 12:
        speak(f"Good Morning {MASTER}, now the time is {strTime}")
        weather()

    elif hour >= 12 and hour < 18:
        speak(f"Good Afternoon {MASTER}, now the time is {strTime}")
        weather()

    else:
        speak(f"Good Evening {MASTER}, now the time is {strTime}")
        weather()

    speak("jarvis at your service")


if __name__ == "__main__":
    takeAuth()
