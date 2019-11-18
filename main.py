import random
import time
import pyautogui
import speech_recognition as sr #speech recognition
import os
from pywinauto import application 
import win32com.client as wincl #voice output
import pyttsx3 #voice output
import random


from gtts import gTTS

def recognize_speech_from_mic(recognizer, microphone):
	
    """Transcribe speech from recorded from `microphone`.

    Returns a dictionary with three keys:
    "success": a boolean indicating whether or not the API request was
               successful
    "error":   `None` if no error occured, otherwise a string containing
               an error message if the API could not be reached or
               speech was unrecognizable
    "transcription": `None` if speech could not be transcribed,
               otherwise a string containing the transcribed text
    """
    # check that recognizer and microphone arguments are appropriate type

    if not isinstance(recognizer, sr.Recognizer):
        raise TypeError("`recognizer` must be `Recognizer` instance")

    if not isinstance(microphone, sr.Microphone):
        raise TypeError("`microphone` must be `Microphone` instance")

    # adjust the recognizer sensitivity to ambient noise and record audio
    # from the microphone
    with microphone as source:
        recognizer.adjust_for_ambient_noise(source,duration=5)
        audio = recognizer.listen(source)

    # set up the response object
    response = {
        "success": True,
        "error": None,
        "transcription": None
    }

    # try recognizing the speech in the recording
    # if a RequestError or UnknownValueError exception is caught,
    #     update the response object accordingly
    try:
        response["transcription"] = recognizer.recognize_google(audio)
    except sr.RequestError:
        # API was unreachable or unresponsive
        response["success"] = False
        response["error"] = "API unavailable"
    except sr.UnknownValueError:
        # speech was unintelligible
        response["error"] = "Unable to recognize speech"

    return response


if __name__ == "__main__":
	
	# set the list of words, maxnumber of guesses, and prompt limit
	# WORDS = ["apple", "banana", "grape", "orange", "mango", "lemon"]
	# NUM_GUESSES = 3
	# PROMPT_LIMIT = 5

	# create recognizer and mic instances
	recognizer = sr.Recognizer()
	microphone = sr.Microphone()

	# get a random word from the list
	#word = random.choice(WORDS)

	# format the instructions string
	# instructions = (
	#     "I'm thinking of one of these words:\n"
	#     "{words}\n"
	#     "You have {n} tries to guess which one.\n"
	# ).format(words=', '.join(WORDS), n=NUM_GUESSES)

	# show instructions and wait 3 seconds before starting the game
	#print(instructions)
	#time.sleep(3)
	#speak = wincl.Dispatch("SAPI.SpVoice")
	data = pyttsx3.init()
	#d = str(random.randrange(100, 1000, 2))
	
	guess = recognize_speech_from_mic(recognizer, microphone)
	if guess["transcription"].lower() == 'hey, rups':
		print('you said',guess["transcription"])
		data.say(guess["transcription"])
		data.runAndWait()
		#speak.Speak(guess["transcription"])
		if guess["transcription"].lower()=='take a screenshot':
			img = pyautogui.screenshot()
			img.save(r"C:\Users\rupam\Pictures\screenshot_"+str(random.randint(0,9))+'.png')
			print('Screenshot done')
		if guess["transcription"].lower()=='please open the google chrome':
			pyautogui.moveTo(1200, 1050, duration = 5)
			pyautogui.click(1200, 1050)
		if guess["transcription"].lower()=='restart my system':
			os.system("shutdown /r /t 1");
		if guess["transcription"].lower()=='open notepad':
			data.say("ok sir, i am opening your notepad")
			data.runAndWait()
			app =  application.Application()
			app.start("Notepad.exe")
		if guess["transcription"].lower()=='open chrome':
			app =  application.Application()
			app.start("C:\Program Files (x86)\Google\Chrome\Application\chrome.exe")
		if guess["transcription"].lower()=='open sublime text':
			app =  application.Application()
			app.start("C:\Program Files\Sublime Text 3\sublime_text.exe") 
	else:
		print('')
