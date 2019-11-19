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




# Text to voice conversion

try:
    engine = pyttsx3.init()
except ImportError:
    print('Request driver is not found')
except RuntimeError:
    print('Driver fails to initilize')
#voices = engine.getProperty('voices')
# for voice in voices:
#     print('voice',voice.id)      
engine.setProperty('voice','HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0')
rate = engine.getProperty('rate')
#print('rate',rate)
engine.setProperty('rate',150)
#ttx.runAndWait()

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    print('wisme')
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning")

    elif hour>=12 and hour<=18:
        speak('Good Afternoon')
    else:
        speak('Good Evening')
    
    speak('I am ram Sir. Please tell me how may i help you')


# Record audio and return it as a string
def takeCommand():
    r = sr.Recognizer()
    print('list',sr.Microphone().list_microphone_names())
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
        print("Request results from Google Speech Recognition service"+e)
    except sr.UnknownValueError:
        # speech was unintelligible
        print("Sorry about that, i didn't hear anything")
        #ttx.say(txt)

    return ""




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
    if(wakeWord(waketext) == True):
        while True:

            #Check for the wake word/pharse

            print('ddddddddddddddd')
            text = takeCommand().lower()
            print('text',text)

            # check the see if the user said anything about date
            if ('date' in text):
                get_date  = getDate()
                response = response + ' ' + get_date
            
            #Have the assistant respond back using audio and the text
            elif ('time' in text):
                now = datetime.datetime.now()
                meridiem = ''
                if now.hour >= 12:
                    meridiem  = 'p.m'
                    hour = now.hour -12
                else:
                    meridiem = 'a.m'
                response = response + 'It is '+ str(hour) +':'+str(now.minute)+' '+meridiem+' .'
            
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
                img = pyautogui.screenshot()
                img.save(r"C:\Users\rupam\Pictures\screenshot_"+str(random.randint(0,9))+'.png')
                print('Screenshot done')
            
            elif 'restart' in text.lower():
                os.system("shutdown /r /t 1")

            elif 'notepad' in text.lower():
                app =  application.Application()
                app.start("Notepad.exe")

            elif 'chrome' in text.lower():
                print('text1111111',text)
                app =  application.Application()
                app.start("C:\Program Files (x86)\Google\Chrome\Application\chrome.exe")
                    
            elif 'search' in text.lower():
                search_terms = text.replace('search ','')
                print('search_terms',search_terms)
                url = "https://www.google.com.tr/search?q={}".format(search_terms)
                webbrowser.open_new_tab(url)

            elif 'open youtube' in text.lower():
                txt = "do you want listen or search anything?"
                print(txt)
                speak(txt)
                engine.runAndWait()
                if text.lower() == "yes":
                    txt = "Please tell me what do you want to listen or play?"
                    print(txt)
                    speak(txt)
                    engine.runAndWait()
                    speak("ok, sir")
                    #search_terms = text.replace('open youtube and search ','')
                    url = "https://www.youtube.com/results?search_query={}".format(text.lower())
                    webbrowser.open_new_tab(url)

                elif text.lower() == "no":
                    txt = 'ok, sir'
                    print(txt)
                    speak(txt)
                    url = "https://www.youtube.com/"
                    webbrowser.open_new_tab(url)

            elif 'open' in text.lower():
                os.system('explorer C:\\"{}"'.format(text.replace('Open ','')))

            elif 'sublime' in text.lower():
                app =  application.Application()
                app.start("C:\Program Files\Sublime Text 3\sublime_text.exe") 
    else:
        speak('Sorry, I am not able to recognise you!!')
            