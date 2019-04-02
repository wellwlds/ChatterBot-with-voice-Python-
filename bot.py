from chatterbot.trainers import ListTrainer
from chatterbot import ChatBot
import logging 
from gtts import gTTS
import os
import speech_recognition as sr

logging.basicConfig(level=logging.CRITICAL)

def py_error_handler(filename, line, function, err, fmt):
	print("");

r = sr.Recognizer()

bot = ChatBot('Bot')

trainer = ListTrainer(bot)

trainer.train(["Hi","Hi. How are you?"])

while True:
	with sr.Microphone() as source:
		print("Say something");
		audio = r.listen(source);
		print(r.recognize_google(audio,language = 'pt-BR'))
		print("Thinking...");
	
	resposta = bot.get_response(r.recognize_google(audio,language = 'pt-BR'))
	
	print('Bot: ', resposta)
	tts = gTTS(text=resposta.text, lang='pt')
	tts.save("said.mp3")
	os.system("mpg321 said.mp3")