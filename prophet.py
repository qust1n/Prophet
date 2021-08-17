from pyrogram import Client, filters, errors
from pydub import AudioSegment
import speech_recognition as sr
from colorama import Fore, Style
from setlang import LangIndex
from  art import *
import os 

os.system('cls' if os.name == 'nt' else 'clear')

tprint("PROPHET")
tprint("by QSST", "cybermedium")

app = Client("my_account")

try:
	@app.on_message(filters.voice)
	def speech(_, msg):
			
		def progress(current, total): 
			print(f"{current * 100 / total:.1f}%") 
			
		file_name = 'speak.ogg'
		app.download_media(msg.voice, file_name, progress=progress)
			
			
		song = AudioSegment.from_ogg("./downloads/speak.ogg")
		song.export("./downloads/speak.wav", format="wav")
			
		AUDIO_FILE = "./downloads/speak.wav"
						  	  			  	  			  	  
		r = sr.Recognizer()
		with sr.AudioFile(AUDIO_FILE) as source:
			audio = r.record(source) 
		try:
		
			msg.reply("<i>Voice from: "+ "**"+msg.from_user.username+"**"+"</i>" + 
								"\n\n" + r.recognize_google(audio, language = LangIndex))
					  	  			  	  			  	  			  	  			  	  			  	  			  	  			  	  			  	  
		except sr.UnknownValueError: 
			print("Google Speech Recognition could not understand audio")
			
		except sr.RequestError as e:
			print("Could not request results from Google Speech Recognition service; {0}".format(e))
		
	#print(Style.BRIGHT + Fore.CYAN + '[' + Fore.YELLOW + '☆' + Fore.GREEN 
							#+ ' Created by QUSTIN ' + Fore.YELLOW + '☆' + Fore.CYAN + ']')				
						
	app.run()
		
except:
	app.restart()
	print("Userbot restarted")