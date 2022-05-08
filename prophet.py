from pyrogram import Client, filters
from pydub import AudioSegment
import speech_recognition as sr
import os 
import asyncio
from tqdm import trange
from asciimatics.effects import Cycle, Stars
from asciimatics.renderers import FigletText
from asciimatics.scene import Scene
from asciimatics.screen import Screen
from art import *
from config import api_id, api_hash
from rich.console import Console 
import base64	

decodedBytes = base64.b64decode(api_id)
decodedStr = int(decodedBytes)
	
decodedBytes2 = base64.b64decode(api_hash)
decodedStr2 = str(decodedBytes2, "utf-8")


if os.path.exists("lang.py") == False:

	with open('lang.py', 'w') as file:
		file.write("LanIndex = " + "'en-US")

else:

	pass

try:

	from lang import LanIndex

except:

	with open('lang.py', 'w') as file:
		file.write("LanIndex = " + "'en-US'")
	from lang import LanIndex

os.system('cls' if os.name == 'nt' else 'clear')

tprint("PROPHET")
tprint("by QSST", "cybermedium")

print('\033[3mTo change the language, write \033[32m.l "number"\033[0m\033[3m from the list in any telegram chat.\n'+
          "To view the list, write in any telegram chat \033[32m.list\033[0m\033[3m\n\nDefault: \033[32mEnglish (United Kingdom)\033[0m")

console = Console()

app = Client("my_account", 
						api_id=decodedBytes, 
						api_hash=decodedBytes2, 
						lang_code="ru")

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

print("\n\033[3mNow: " + LanIndex)

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
		
		await msg.reply("**Recognized: <i>**\n" + r.recognize_google(audio, language = LanIndex) + "</i>", quote=True)
		
		await msg.react("🔥")	  			  	  			  	  			  	  			  	  			  	  			  	  			  	  			  	  
	
	except sr.UnknownValueError: 
		await msg.reply("__Speech Recognition could not understand audio__", quote=True)
	
	except sr.RequestError as e:
		await msg.reply("__Could not request results from Google Speech Recognition service; {0}__".format(e), quote=True)		

@app.on_message(filters.command("l", prefixes=".") & filters.me)
async def change_language(_, msg):
	
	try:
		LangIndex = ""
		
		orig_text = msg.text.split(".l ", maxsplit=1)[1]
		a = orig_text
		a = int(a)
			
		await msg.delete()
		
		if a == 1:
			LangIndex = "af-ZA"
		elif a == 2:
			LangIndex = "sq-AL"
		elif a == 3:
			LangIndex = "am-ET"
		elif a == 4:
			LangIndex = "ar-DZ"
		elif a == 5:
			LangIndex = "ar-BH"
		elif a == 6:
			LangIndex = "ar-EG"
		elif a == 7:
			LangIndex = "ar-IQ"
		elif a == 8:
			LangIndex = "ar-IL"
		elif a == 9:
			LangIndex = "ar-JO"
		elif a == 10:
			LangIndex = "ar-KW"
		elif a == 11:
			LangIndex = "ar-LB"
		elif a == 12:
			LangIndex = "ar-MA"
		elif a == 13:
			LangIndex = "ar-OM"
		elif a == 14:
			LangIndex = "ar-QA"
		elif a == 15:
			LangIndex = "ar-SA"
		elif a == 16:
			LangIndex = "ar-PS"
		elif a == 17:
			LangIndex = "ar-TN"
		elif a == 18:
			LangIndex = "ar-AE"
		elif a == 19:
			LangIndex = "ar-YE"
		elif a == 20:
			LangIndex = "hy-AM"
		elif a == 21:
			LangIndex = "az-AZ"
		elif a == 22:
			LangIndex = "eu-ES"
		elif a == 23:
			LangIndex = "bn-BD"
		elif a == 24:
			LangIndex = "bn-IN"
		elif a == 25:
			LangIndex = "bs-BA"
		elif a == 26:
			LangIndex = "bg-BG"
		elif a == 27:
			LangIndex = "my-MM"
		elif a == 28:
			LangIndex = "ca-ES"
		elif a == 29:
			LangIndex = "yue-Hant-HK"
		elif a == 30:
			LangIndex = "zh (cmn-Hans-CN)"
		elif a == 31:
			LangIndex = "zh-TW (cmn-Hant-TW)"
		elif a == 32:
			LangIndex = "hr-HR"
		elif a == 33:
			LangIndex = "cs-CZ"
		elif a == 34:
			LangIndex = "da-DK"
		elif a == 35:
			LangIndex = "nl-BE"
		elif a == 36:
			LangIndex = "nl-NL"
		elif a == 37:
			LangIndex = "en-AU"
		elif a == 38:
			LangIndex = "en-CA"
		elif a == 39:
			LangIndex = "en-GH"
		elif a == 40:
			LangIndex = "en-HK"
		elif a == 41:
			LangIndex = "en-IN"
		elif a == 42:
			LangIndex = "en-IE"
		elif a == 43:
			LangIndex = "en-KE"
		elif a == 44:
			LangIndex = "en-NZ"
		elif a == 45:
			LangIndex = "en-NG"
		elif a == 46:
			LangIndex = "en-PK"
		elif a == 47:
			LangIndex = "en-PH"
		elif a == 48:
			LangIndex = "en-SG"
		elif a == 49:
			LangIndex = "en-ZA"
		elif a == 50:
			LangIndex = "en-TZ"
		elif a == 51:
			LangIndex = "en-GB"
		elif a == 52:
			LangIndex = "en-US"
		elif a == 53:
			LangIndex = "et-EE"
		elif a == 54:
			LangIndex = "fil-PH"
		elif a == 55:
			LangIndex = "fi-FI"
		elif a == 56:
			LangIndex = "fr-BE"
		elif a == 57:
			LangIndex = "fr-CA"
		elif a == 58:
			LangIndex = "fr-FR"
		elif a == 59:
			LangIndex = "fr-CH"
		elif a == 60:
			LangIndex = "gl-ES"
		elif a == 61:
			LangIndex = "ka-GE"
		elif a == 62:
			LangIndex = "de-AT"
		elif a == 63:
			LangIndex = "de-DE"
		elif a == 64:
			LangIndex = "de-CH"
		elif a == 65:
			LangIndex = "el-GR"
		elif a == 66:
			LangIndex = "gu-IN"
		elif a == 67:
			LangIndex = "iw-IL"
		elif a == 68:
			LangIndex = "hi-IN"
		elif a == 69:
			LangIndex = "hu-HU"
		elif a == 70:
			LangIndex = "is-IS"
		elif a == 71:
			LangIndex = "id-ID"
		elif a == 72:
			LangIndex = "it-IT"
		elif a == 73:
			LangIndex = "it-CH"
		elif a == 74:
			LangIndex = "ja-JP"
		elif a == 75:
			LangIndex = "jv-ID"
		elif a == 76:
			LangIndex = "kn-IN"
		elif a == 77:
			LangIndex = "kk-KZ"
		elif a == 78:
			LangIndex = "km-KH"
		elif a == 79:
			LangIndex = "ko-KR"
		elif a == 80:
			LangIndex = "lo-LA"
		elif a == 81:
			LangIndex = "lv-LV"
		elif a == 82:
			LangIndex = "lt-LT"
		elif a == 83:
			LangIndex = "mk-MK"
		elif a == 84:
			LangIndex = "ms-MY"
		elif a == 85:
			LangIndex = "ml-IN"
		elif a == 86:
			LangIndex = "mr-IN"
		elif a == 87:
			LangIndex = "mn-MN"
		elif a == 88:
			LangIndex = "ne-NP"
		elif a == 89:
			LangIndex = "no-NO"
		elif a == 90:
			LangIndex = "fa-IR"
		elif a == 91:			
			LangIndex = "pl-PL"
		elif a == 92:
			LangIndex = "pt-BR"
		elif a == 93:
			LangIndex = "pt-PT"
		elif a == 94:
			LangIndex = "pa-Guru-IN"
		elif a == 95:
			LangIndex = "ro-RO"
		elif a == 96:
			LangIndex = "ru-RU"
		elif a == 97:
			LangIndex = "sr-RS"
		elif a == 98:
			LangIndex = "si-LK"
		elif a == 99:
			LangIndex = "sk-SK"
		elif a == 100:
			LangIndex = "sl-SI"
		elif a == 101:
			LangIndex = "es-AR"
		elif a == 102:
			LangIndex = "es-BO"
		elif a == 103:
			LangIndex = "es-CL"
		elif a == 104:
			LangIndex = "es-CO"
		elif a == 105:
			LangIndex = "es-CR"
		elif a == 106:
			LangIndex = "es-DO"
		elif a == 107:
			LangIndex = "es-EC"
		elif a == 108:
			LangIndex = "es-SV"
		elif a == 109:
			LangIndex = "es-GT"
		elif a == 110:
			LangIndex = "es-HN"
		elif a == 111:
			LangIndex = "es-MX"
		elif a == 112:
			LangIndex = "es-NI"
		elif a == 113:
			LangIndex = "es-PA"
		elif a == 114:
			LangIndex = "es-PY"
		elif a == 115:
			LangIndex = "es-PE"
		elif a == 116:
			LangIndex = "es-PR"
		elif a == 117:
			LangIndex = "es-ES"
		elif a == 118:
			LangIndex = "es-US"
		elif a == 119:
			LangIndex = "es-UY"
		elif a == 120:
			LangIndex = "es-VE"
		elif a == 121:
			LangIndex = "su-ID"
		elif a == 122:
			LangIndex = "sw-KE"
		elif a == 123:
			LangIndex = "sw-TZ"
		elif a == 124:
			LangIndex = "sv-SE"
		elif a == 125:
			LangIndex = "ta-IN"
		elif a == 126:
			LangIndex = "ta-MY"
		elif a == 127:
			LangIndex = "ta-SG"
		elif a == 128:
			LangIndex = "ta-LK"
		elif a == 129:
			LangIndex = "te-IN"
		elif a == 130:
			LangIndex = "th-TH"
		elif a == 131:
			LangIndex = "tr-TR"
		elif a == 132:
			LangIndex = "uk-UA"
		elif a == 133:
			LangIndex = "ur-IN"
		elif a == 134:
			LangIndex = "ur-PK"
		elif a == 135:
			LangIndex = "uz-UZ"
		elif a == 136:
			LangIndex = "vi-VN"
		elif a == 137:
			LangIndex = "zu-ZA"
		
		with open('lang.py', 'w') as file:
			file.write("LanIndex = " + "'" + LangIndex + "'")
		global LanIndex
		LanIndex = LangIndex
		await msg.reply("**Changed to: **" + LanIndex)
		print("\n\033[3mChanged to: " + LanIndex)
	
	except Exception:
		console.print_exception(show_locals=True)
		
@app.on_message(filters.command("list", prefixes=".") & filters.me)
async def languages_list(_, msg):
	
	await msg.edit("List of languages:\n\n"+
							'1. Afrikaans (South Africa)\n'+
							'2. Albanian (Albania)\n'+
							'3. Amharic (Ethiopia)\n'+
							'4. Arabic (Algeria)\n'+
							'5. Arabic (Bahrain)\n'+
							'6. Arabic (Egypt)\n'+
							'7. Arabic (Iraq)\n'+
							'8. Arabic (Israel)\n'+
							'9. Arabic (Jordan)\n'+
							"10. Arabic (Kuwait)\n"+
							"11. Arabic (Lebanon)\n"+
							"12. Arabic (Morocco)\n"+
							"13. Arabic (Oman)\n"+
							"14. Arabic (Qatar)\n"+
							"15. Arabic (Saudi Arabia)\n"+
							"16. Arabic (State of Palestine)\n"+
							"17. Arabic (Tunisia)\n"+
							"18. Arabic (United Arab Emirates)\n"+
							"19. Arabic (Yemen)\n"+
							"20. Armenian (Armenia)\n"+
							"21. Azerbaijani (Azerbaijan)\n"+
							"22. Basque (Spain)\n"+
							"23. Bengali (Bangladesh)\n"+
							"24. Bengali (India)\n"+
							"25. Bosnian (Bosnia and Herzegovina)\n"+
							"26. Bulgarian (Bulgaria)\n"+
							"27. Burmese (Myanmar)\n"+
							"28. Catalan (Spain)\n"+
							"29. Chinese, Cantonese (Traditional Hong Kong)\n"+
							"30. Chinese, Mandarin (Simplified, China)\n"+
							"31. Chinese, Mandarin (Traditional, Taiwan)\n"+
							"32. Croatian (Croatia)\n"+
							"33. Czech (Czech Republic)\n"+
							"34. Danish (Denmark)\n"+
							"35. Dutch (Belgium)\n"+
							"36. Dutch (Netherlands)\n"+
							"37. English (Australia)\n"+
							"38. English (Canada)\n"+
							"39. English (Ghana)\n"+
							"40. English (Hong Kong)\n"+
							"41. English (India)\n"+
							"42. English (Ireland)\n"+
							"43. English (Kenya)\n"+
							"44. English (New Zealand)\n"+
							"45. English (Nigeria)\n"+
							"46. English (Pakistan)\n"+
							"47. English (Philippines)\n"+
							"48. English (Singapore)\n"+
							"49. English (South Africa)\n"+
							"50. English (Tanzania)\n"+
							"51. English (United Kingdom)\n"+
							"52. English (United States)\n"+
							"53. Estonian (Estonia)\n"+
							"54. Filipino (Philippines)\n"+
							"55. Finnish (Finland)\n"+
							"56. French (Belgium)\n"+
							"57. French (Canada)\n"+
							"58. French (France)\n"+
							"59. French (Switzerland)\n"+
							"60. Galician (Spain)\n"+
							"61. Georgian (Georgia)\n"+
							"62. German (Austria)\n"+
							"63. German (Germany)\n"+
							"64. German (Switzerland)\n"+
							"65. Greek (Greece)\n"+
							"66. Gujarati (India)\n"+
							"67. Hebrew (Israel)\n"+
							"68. Hindi (India)\n"+
							"69. Hungarian (Hungary)\n"+
							"70. Icelandic (Iceland)\n"+
							"71. Indonesian (Indonesia)\n"+
							"72. Italian (Italy)\n"+
							"73. Italian (Switzerland)\n"+
							"74. Japanese (Japan)\n"+
							"75. Javanese (Indonesia)\n"+
							"76. Kannada (India)\n"+
							"77. Kazakh (Kazakhstan)\n"+
							"78. Khmer (Cambodia)\n"+
							"79. Korean (South Korea)\n"+
							"80. Lao (Laos)\n"+
							"81. Latvian (Latvia)\n"+
							"82. Lithuanian (Lithuania)\n"+
							"83. Macedonian (North Macedonia)\n"+
							"84. Malay (Malaysia)\n"+
							"85. Malayalam (India)\n"+
							"86. Marathi (India)\n"+
							"87. Mongolian (Mongolia)\n"+
							"88. Nepali (Nepal)\n"+
							"89. Norwegian Bokmål (Norway)\n"+
							"90. Persian (Iran)\n"+
							"91. Polish (Poland)\n"+
							"92. Portuguese (Brazil)\n"+
							"93. Portuguese (Portugal)\n"+
							"94. Punjabi (Gurmukhi India)\n"+
							"95. Romanian (Romania)\n"+
							"96. Russian (Russia)\n"+
							"97. Serbian (Serbia)\n"+
							"98. Sinhala (Sri Lanka)\n"+
							"99. Slovak (Slovakia)\n"+
							"100. Slovenian (Slovenia)\n"+
							"101. Spanish (Argentina)\n"+
							"102. Spanish (Bolivia)\n"+
							"103. Spanish (Chile)\n"+
							"104. Spanish (Colombia)\n"+
							"105. Spanish (Costa Rica)\n"+
							"106. Spanish (Dominican Republic)\n"+
							"107. Spanish (Ecuador)\n"+
							"108. Spanish (El Salvador)\n"+
							"109. Spanish (Guatemala)\n"+
							"110. Spanish (Honduras)\n"+
							"111. Spanish (Mexico)\n"+
							"112. Spanish (Nicaragua)\n"+
							"113. Spanish (Panama)\n"+
							"114. Spanish (Paraguay)\n"+
							"115. Spanish (Peru)\n"+
							"116. Spanish (Puerto Rico)\n"+
							"117. Spanish (Spain)\n"+
							"118. Spanish (United States)\n"+
							"119. Spanish (Uruguay)\n"+
							"120. Spanish (Venezuela)\n"+
							"121. Sundanese (Indonesia)\n"+
							"122. Swahili (Kenya)\n"+
							"123. Swahili (Tanzania)\n"+
							"124. Swedish (Sweden)\n"+
							"125. Tamil (India)\n"+
							"126. Tamil (Malaysia)\n"+
							"127. Tamil (Singapore)\n"+
							"128. Tamil (Sri Lanka)\n"+
							"129. Telugu (India)\n"+
							"130. Thai (Thailand)\n"+
							"131. Turkish (Turkey)\n"+
							"132. Ukrainian (Ukraine)\n"+
							"133. Urdu (India)\n"+
							"134. Urdu (Pakistan)\n"+
							"135. Uzbek (Uzbekistan)\n"+
							"136. Vietnamese (Vietnam)\n"+
							"137. Zulu (South Africa)\n\n")

	
	
app.run()
		
