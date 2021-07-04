import os, time; import threading; from tkinter import *

class init:
	def __init__(self,ventana,path,delay=.08):
		global images, b, large, tempo;
		images    = [PhotoImage(file=path+"/"+file) for file in sorted(os.listdir(path))]
		large     = len(images)-1; tempo = delay;
		b         = Label(ventana,image=images[0]); b.place(x=0, y=0)
		self.hilo = thread()
class thread(threading.Thread):
	def run(self):
		global images, large, b, stop, tempo; contador = 0
		try:
			self.stop = 0;
			while self.stop == 0:
				if contador == large: contador = 0
				b.configure(image=images[contador])
				contador += 1
				time.sleep(tempo)
		except: print()
	def stopgif(self):
		global stop
		self.stop = 1
		