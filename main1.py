import random
import time
import pyautogui
import speech_recognition as sr #speech recognition
import os
from gtts import gTTS
import random
import datetime
import calendar
import wikipedia
import pyttsx3 #voice output
import webbrowser
from pywinauto import application
import requests
import pytemperature
import time
from pygame import mixer


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def setBrowser(browser_name):
    if browser_name == 'chrome':
        chrome_path='C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe'
        webbrowser.register('chrome',None,webbrowser.BackgroundBrowser(chrome_path))

def getWheatherDetails(city_name):
    API_KEY = '770436733470f942485967ca3c221b71'
    r = requests.get('http://api.openweathermap.org/data/2.5/weather?q='+city_name+'&appid='+API_KEY)
    r = r.json()
    #print('r',r['main'])
    temp = float(r['main']['temp'])
    temp = pytemperature.k2c(temp)
    details ={
        "temp":temp,
        "humidity":str(r['main']['humidity']),
        "pressure":str(r['main']['pressure'])
    }
    return details

try:

    # Initiate text to voice
    engine = pyttsx3.init()

    # For playing music from pygame
    mixer.init()

    # Chrome browser
    setBrowser('chrome')

    # Check wheather
    wheather_details = getWheatherDetails('kolkata')

except ImportError:
    print('Request driver is not found')
except RuntimeError:
    print('Driver fails to initilize')
#voices = engine.getProperty('voices')
# for voice in voices:
#     print('voice',voice.id)      
engine.setProperty('voice','HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0')
rate = engine.getProperty('rate')
engine.setProperty('rate',140)

def responseMusicEverytime():
    mixer.music.load('robot-e.mp3')
    mixer.music.play()
    time.sleep(2)

def wishMe():
    print('wisme')

    # hour = int(datetime.datetime.now().hour)
    
    # mixer.music.load('robot-e.mp3')
    # mixer.music.play()

    # time.sleep(2.3)
    # speak('Starting all system and applications')
    
    # mixer.music.load('robot-m.mp3')
    # mixer.music.play()
    # time.sleep(17)
    # speak('Checking health of all core processors')
    # engine.runAndWait()
    # speak('All system has been started')
    # mixer.music.load('robot-e.mp3')
    # mixer.music.play()
    # time.sleep(2.3)

    # speak('Now, i am online')
    # speak('Hi i am ram , personal digital assistant') 
    # engine.runAndWait()

    # if hour>=0 and hour<12:
    #     speak("Good Morning")
    # elif hour>=12 and hour<=18:
    #     speak('Good Afternoon')
    # else:
    #     speak('Good Evening')
    
    # print(getDate())
    # speak(getDate())

    # now = time.strftime("%I:%M %p")
    # print('Time is ', now)
    # speak('Time is '+ time.strftime("%I")+time.strftime("%M")+time.strftime("%p"))
    # engine.runAndWait()

    # print('current temparature in your city '+str(wheather_details['temp'])+' degree celcias')
    # speak('current temparature in your city '+str(wheather_details['temp'])+' degree celcias')
    # print('humidity is ' +wheather_details['humidity'])
    # speak('humidity is '+wheather_details['humidity'])
    # print('pressure is ' +wheather_details['pressure'])
    # speak('pressure is '+wheather_details['pressure'])
    # engine.runAndWait()

    # speak('I am ram Sir. Please tell me how may i help you')
   

# Record audio and return it as a string
def takeCommand():
    r = sr.Recognizer()
    #print('list',sr.Microphone().list_microphone_names())
    with sr.Microphone() as source:
        print('Say something')
        r.pause_threshold = 1
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source)

    try:
        print('Recognizing...')
        data = r.recognize_google(audio, language='en-in')
        print('You said',data)
        return data
    except sr.RequestError as e:
        # API was unreachable or unresponsive
        print("Could not request results from Google Speech Recognition service; {0}".format(e))
    except sr.UnknownValueError:
        # speech was unintelligible
        print("Google Speech Recognition could not understand audio")
        #ttx.say(txt)
    return ''

# A function to check if the users command/text contains a wake word/pharse
def wakeWord(text):
	WAKE_WORDS = ['hi ram','okay ram']
	text =  text.lower()
	for pharse in WAKE_WORDS:
		if pharse in text:
			return True
	return False

# A function to get the date
def getDate():
    now = datetime.datetime.now()
    my_date = datetime.datetime.today()
    weekday = calendar.day_name[my_date.weekday()]
    monthNum = now.month
    dayNum = now.day

    # A List of months 
    month_names = ['January','February','March','April','May','June','July','Auguest','September','October','November','December']

    # A list of ordinal numbers

    ordinalNumbers = ['1st','2nd','3rd','4th','5th','6th','7th','8th','9th','10th','11th','12th',
    '13th','14th','15th','16th','17th','18th','19th','20th','21st','22nd','23rd','24th','25th','26th',
    '27th','28th','29th','30th','31st']

    return 'Today is '+weekday+' and '+ordinalNumbers[dayNum-1]+' of '+month_names[monthNum-1]+'.'

# Function to return a random greeting response 
def greeting(text):
    # greeting inputs
    GREETING_INPUTS = ['hi','hey','hola','greetings','wassup','hello','whatsapp']

    # Greetings response back to the user
    GREETING_RESPONSES = ['howdy','whats good','hello','hey there']

    # if the users input is a greeting, then return a randomly choosen greetings response
    for word in text.split():
        if word.lower() in GREETING_INPUTS:
            return random.choice(GREETING_RESPONSES)+"."
    
    # If no greeting was detected then return an empty string
    return ''

# A function to get information from a person

def getPerson(text):
    wordList = text.split() # Split the text into list of words
    for i in range(0, len(wordList)):
        if i + 3 <= len(wordList) - 1 and  wordList[i].lower() == 'who' and wordList[i+1].lower() == 'is':
            return wordList[i+2]+ ' ' + wordList[i+3]

if __name__ == "__main__":
    wishMe()
    
    waketext = takeCommand().lower()
    print('waketext',waketext)
    if(wakeWord(waketext) == True):
        while True:
            #Check for the wake word/pharse

            responseMusicEverytime()
            print('I am ready to listen you..')
            speak('I am ready to listen you..')

            text = takeCommand().lower()
            #print('text',text)

            # check the see if the user said anything about date
            if ('date' in text):
                get_date  = getDate()
                time.sleep(1)
                speak(get_date)
            
            #Have the assistant respond back using audio and the text
            elif ('time' in text):
                now = datetime.datetime.now()
                meridiem = ''
                if now.hour >= 12:
                    meridiem  = 'p.m'
                    hour = now.hour -12
                else:
                    meridiem = 'a.m'
                time = 'It is '+ str(hour) +':'+str(now.minute)+' '+meridiem+' .'
                print('current time is',time)
                speak(time)
            
            # Check to see if the user said 'who is'
            elif('who is' in text):
                person = getPerson(text)
                print('person',person)
                if person:
                    wiki = wikipedia.summary(person, sentences=2)
                    print('wiki',wiki)
                    response = response + ' '+ wiki
                print('response',response)

            elif 'take a screenshot' in text.lower():
                speak("ok sir, please wait..")
                time.sleep(2)
                img = pyautogui.screenshot()
                img.save(r"C:\Users\rupam\Pictures\screenshot_"+str(random.randint(0,9))+'.png')
                print('Screenshot done')
            
            elif 'shutdown' in text.lower():
                speak("ok sir, please wait i am shutdown your computer..")
                time.sleep(2)   
                os.system("shutdown /s /t 1");
            
            elif 'restart' in text.lower():
                speak("ok sir, please wait i am restarting your computer..")
                time.sleep(2) 
                os.system("shutdown /r /t 1")

            elif 'notepad' in text.lower():
                app =  application.Application()
                app.start("Notepad.exe")
                    
            elif 'open chrome' in text.lower():
                txt = "Do you want to search anything?"
                print(txt)
                speak(txt)
                text = takeCommand().lower()
                engine.runAndWait()

                if text.lower() == "yes":
                    txt = "Please tell me what do you want to search?"
                    print(txt)
                    speak(txt)
                    text = takeCommand().lower()
                    search_terms = text.replace('search ','')
                    speak("ok sir, please wait i am searching your text in chrome..")
                    engine.runAndWait()
                    url = "https://www.google.com/search?q={}".format(search_terms)
                    webbrowser.get('chrome').open(url)

                elif text.lower() == "no":
                    speak("ok sir, please wait i am opening chrome..")
                    engine.runAndWait()
                    url = "https://www.google.com/"
                    webbrowser.get('chrome').open(url)

            elif 'open youtube' in text.lower():
                txt = "Do you want to listen or search anything?"
                print(txt)
                speak(txt)
                text = takeCommand().lower()
                engine.runAndWait()
                print('check',text)
                if text.lower() == "yes":
                    txt = "Please tell me what do you want to listen or play?"
                    print(txt)
                    speak(txt)
                    text = takeCommand().lower()
                    speak("ok sir, i am opening youtube")
                    engine.runAndWait()
                    url = "https://www.youtube.com/results?search_query={}".format(text)
                    webbrowser.open_new_tab(url)

                elif text.lower() == "no":
                    txt = 'ok sir, i am opening youtube'
                    print(txt)
                    speak(txt)
                    engine.runAndWait()
                    url = "https://www.youtube.com/"
                    webbrowser.open_new_tab(url)

            elif 'sublime' in text.lower():
                app =  application.Application()
                app.start("C:\Program Files\Sublime Text 3\sublime_text.exe")  
            
            elif 'open' in text.lower():
                speak("ok sir, please wait..")
                time.sleep(2)
                os.system('explorer C:\\"{}"'.format(text.replace('Open ','')))
    # else:
    #     takeCommand().lower()
    #     speak('Sorry, I am not able to recognise you!!')
            