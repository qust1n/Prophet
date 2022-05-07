from pyrogram import Client, filters
from pydub import AudioSegment
import speech_recognition as sr
from setlang import LangIndex
import os 
import asyncio
from tqdm import trange
from config import api_id, api_hash
from asciimatics.effects import Cycle, Stars
from asciimatics.renderers import FigletText
from asciimatics.scene import Scene
from asciimatics.screen import Screen
from art import *

os.system('cls' if os.name == 'nt' else 'clear')

tprint("PROPHET")
tprint("by QSST", "cybermedium")



app = Client("my_account", api_id=api_id, api_hash=api_hash, lang_code="ru")

def update_screen(end_time, loop, screen):
    screen.draw_next_frame()
    if loop.time() < end_time:
        loop.call_later(0.05, update_screen, end_time, loop, screen)
    else:
        loop.stop()


# Define the scene that you'd like to play.
screen = Screen.open()
effects = [
    Cycle(
        screen,
        FigletText("PROPHET", font='big'),
        screen.height // 2 - 8),
    Cycle(
        screen,
        FigletText("By QSST", font='big'),
        screen.height // 2 + 3),
    Stars(screen, (screen.width + screen.height) // 2)
]
screen.set_scenes([Scene(effects, 500)])

# Schedule the first call to display_date()
loop = asyncio.new_event_loop()
end_time = loop.time() + 2.0
loop.call_soon(update_screen, end_time, loop, screen)

# Blocking call interrupted by loop.stop()
loop.run_forever()
loop.close()
screen.close()



@app.on_message(filters.voice)
async def speech(_, msg):
	
	def progress(current, total): 

		for i in trange(current): 
			...
	
	file_name = 'speak.ogg'
	await app.download_media(msg.voice, file_name, progress=progress)
	
	
	song = AudioSegment.from_ogg("./downloads/speak.ogg")
	song.export("./downloads/speak.wav", format="wav")
	
	AUDIO_FILE = "./downloads/speak.wav"
				  	  			  	  			  	  
	r = sr.Recognizer()
	with sr.AudioFile(AUDIO_FILE) as source:
		audio = r.record(source) 
	try:

		await msg.reply("**Recognized: <i>**\n" + r.recognize_google(audio, language = LangIndex) + "</i>", quote=True)
		
		await msg.react("🔥")	  			  	  			  	  			  	  			  	  			  	  			  	  			  	  			  	  
	
	except sr.UnknownValueError: 
		await msg.reply("__Speech Recognition could not understand audio__", quote=True)
	
	except sr.RequestError as e:
		await msg.reply("__Could not request results from Google Speech Recognition service; {0}__".format(e), quote=True)		
		
	
app.run()
		
