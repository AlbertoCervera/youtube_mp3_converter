from pytube import YouTube
import efectoTipado as type
from moviepy.editor import *
import os
from time import sleep





while True:

	try:
		os.system('cls')
		URL = input("Inserte la url del video > ")
		yt = YouTube(url=URL)
		header = "Descargando sonido del Video..."

		type.escribe_texto(header)

		video = yt.streams.get_audio_only().download()

		mp3 = AudioFileClip(video)

		mp3.write_audiofile(mp3.filename.replace('.mp4', '.mp3'))

		os.remove(mp3.filename)
		os.system("cls")
		
		nextVideo = input("Quieres descargar otro video S/N > ")
		nextVideo = nextVideo.lower()

		if nextVideo == "s":
			os.system("cls")
		elif nextVideo == "n":
			break
		else:
			print("Error escriba 's' o 'n' ")
			break


	except:
		type.escribe_texto("Hemos tenido un problema con la url que ha introducido")
		sleep(2)
		

