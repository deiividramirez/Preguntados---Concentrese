from tkinter import *; from tkinter import messagebox; from numpy import *
from random import shuffle; from time import sleep
import threading, hashlib, json, csv, gif, sys, os

#Variables globales
global usuarios, usuario, contraseña, gif1, gif2

#Contador de Puntajes
class clocktime:
	def __init__(self, ventana, xx=0, yy=0):
		global labeltime
		labeltime = Label(ventana, text=0, width=5)
		labeltime.place(x=xx, y=yy)
		self.hilo = countertime(); self.hilo.start()
class countertime(threading.Thread):
	def run(self):
		global stopper, labeltime, contadortime
		self.stopper = 0; contadortime = 0
		try:
			while self.stopper == 0:
				contadortime += 1
				labeltime.configure(text=contadortime)
				sleep(1)
		except: print("")
	def stoptime(self,nivel,validar):
		global contadortime, stopper, usuarios, usuario
		self.stopper = 1; rjson()
		if validar == True:
			if nivel == 1:
				if contadortime > 0:
					usuarios[encryp(usuario.get())][1] += 10
				elif contadortime > 5:
					usuarios[encryp(usuario.get())][1] += 5
				elif contadortime > 10:
					usuarios[encryp(usuario.get())][1] += 3
			elif nivel == 2:
				if contadortime > 0:
					usuarios[encryp(usuario.get())][1] += 20
				elif contadortime > 5:
					usuarios[encryp(usuario.get())][1] += 10
				elif contadortime > 10:
					usuarios[encryp(usuario.get())][1] += 5
			elif nivel == 3:
				if contadortime > 0:
					usuarios[encryp(usuario.get())][1] += 30
				elif contadortime > 5:
					usuarios[encryp(usuario.get())][1] += 15
				elif contadortime > 10:
					usuarios[encryp(usuario.get())][1] += 5
		if validar == False:
			if nivel == 1:
				if contadortime > 0:
					usuarios[encryp(usuario.get())][1] -= 5
			elif nivel == 2:
				if contadortime > 0:
					usuarios[encryp(usuario.get())][1] -= 10
			elif nivel == 3:
				if contadortime > 0:
					usuarios[encryp(usuario.get())][1] -= 20
		else: 
			pass
		if usuarios[encryp(usuario.get())][1] <= 0:
			usuarios[encryp(usuario.get())][1] = 0
		wjson(usuarios)
#Encriptar objetos / Usuarios y contraseñas
def encryp(a):
	return hashlib.md5(a.encode()).hexdigest()
#Funciones de salir
def salir():
	global gif2; gif2.hilo.stopgif(); sys.exit(1)
def salir1():
	global Game1; ventana.deiconify(); Game1.destroy()
def salir2():
	global Game2; ventana.deiconify(); Game2.destroy()
def salir3():
	global gif1; gif1.hilo.stopgif(); sys.exit(1)
def salir4(e):
	global gifreg, registry, contra, login, gif2;
	login.deiconify();
	if e == 1: 
		gifreg.hilo.stopgif(); registry.destroy()
	if e == 2:
		gifreg.hilo.stopgif(); contra.destroy()
	loginv()
def salir5():
	global Game1, GL; Game1.deiconify(); GL.destroy()
def salir6():
	global Game2, CN; Game2.deiconify(); CN.destroy()
#Funciones para que aparezca usuario / contraseña
def in_usuario(*args):
	if not usuario.get() or usuario.get() == "Usuario": 
		usuario.delete('0', 'end')
def out_usuario(*args):
    if not usuario.get():
    	usuario.insert(0,"Usuario")
def in_contrasena(*args):
	if not contraseña.get() or contraseña.get() == "Contraseña":
		contraseña.delete('0', 'end')
		contraseña.configure(show="*")
def out_contrasena(*args):
    if not contraseña.get():
    	contraseña.insert(0,"Contraseña")
    	contraseña.configure(show="")
#Función que lee el Json
def rjson():
	global usuarios
	try:
		with open('usuarios.json', 'r+') as archivo: usuarios = json.load(archivo)
	except:
		messagebox.showerror("Error", "No existe el archivo.\nSe creará uno."); wjson({})
#Función que escribe el Json
def wjson(txt):
	try:
		with open('usuarios.json', 'w') as archivo: n = json.dump(txt, archivo)
	except:
		messagebox.showerror("Error","No se pudo escribir archivo")
#Función que registra nuevos usuarios
def registro():
	global newusuario, newcontraseña, newoksesion, registry, login, gifreg
	def in_usuarioreg(*args):
		if not newusuario.get() or newusuario.get() == "Usuario": 
			newusuario.delete('0', 'end')
	def out_usuarioreg(*args):
	    if not newusuario.get():
	    	newusuario.insert(0,"Usuario")
	def in_contrasenareg(*args):
		if not newcontraseña.get() or newcontraseña.get() == "Contraseña":
			newcontraseña.delete('0', 'end')
			newcontraseña.configure(show="*")
	def out_contrasenareg(*args):
	    if not newcontraseña.get():
	    	newcontraseña.insert(0,"Contraseña")
	    	newcontraseña.configure(show="")
	login.withdraw();
	registry      = Toplevel(); registry.title("Registrar usuario"); registry.geometry("340x220")
	gifreg        = gif.init(registry, "../Project/Supplies/VentanaRegistro")
	newusuario    = Entry(registry, justify="center", bg="black", foreground="white"); newusuario.place(x=40, y=160)
	newcontraseña = Entry(registry, justify="center", bg="black", foreground="white"); newcontraseña.place(x=40, y=190)
	newoksesion   = Button(registry, text="Registrar", command=registrar, bg="black", foreground="white"); newoksesion.place(x=180, y=175)
	newusuario.insert(0,"Usuario"); newcontraseña.insert(0,"Contraseña")
	newusuario.bind("<FocusIn>", in_usuarioreg); newusuario.bind("<FocusOut>", out_usuarioreg)
	newcontraseña.bind("<FocusIn>", in_contrasenareg); newcontraseña.bind("<FocusOut>", out_contrasenareg)
	registry.protocol('WM_DELETE_WINDOW',lambda a=1:salir4(a))
	registry.resizable(width=False, height=False);
	gifreg.hilo.start()
#Función que registra los usuarios nuevos
def registrar(e = 1):
	global usuarios, newusuario, newcontraseña, newoksesion, registryusuario, contraseña, contra;
	global contra, contrausuario, contracontraseña, contranewcontraseña; rjson()
	if e == 1:
		try: 
			if encryp(newusuario.get()) not in usuarios and newusuario.get != "":
				if newcontraseña.get() != "":
					usuarios[encryp(newusuario.get())] = [encryp(newcontraseña.get()),0,1,1]
					usuario.delete(0,END); contraseña.delete(0,END)
					usuario.insert(0,"Usuario"); contraseña.insert(0,"Contraseña")
					messagebox.showinfo("Información","Se ha creado el usuario, ya puede iniciar sesión")
					wjson(usuarios); registry.destroy(); loginv()
				else:
					messagebox.showerror("Error","No escribió ninguna contraseña")
			else:
				messagebox.showinfo("Información","El usuario ya existe")
		except: print("")
	else:
		try:
			if encryp(contrausuario.get()) in usuarios:
				if encryp(contracontraseña.get()) == usuarios[encryp(contrausuario.get())][0]:
					usuarios[encryp(contrausuario.get())][0] = encryp(contranewcontraseña.get())
					messagebox.showinfo("Existosamente","Se cambió la contraseña.")
					usuario.delete(0,END); contraseña.delete(0,END)
					usuario.insert(0,"Usuario"); contraseña.insert(0,"Contraseña")
					wjson(usuarios); contra.destroy(); loginv()
				else:
					messagebox.showerror("Error","Contraseña erronea")
			else:
				messagebox.showerror("Error","El usuario no existe")
		except: print("")
#Función que cambia la contraseña de un usuario
def contrasena():
	global contra, contrausuario, contracontraseña, contranewcontraseña, login, gifreg
	def in_usuariocontra(*args):
		if not contrausuario.get() or contrausuario.get() == "Usuario": 
			contrausuario.delete('0', 'end')
	def out_usuariocontra(*args):
	    if not contrausuario.get():
	    	contrausuario.insert(0,"Usuario")
	def in_contrasenacontra(*args):
		if not contracontraseña.get() or contracontraseña.get() == "Contraseña":
			contracontraseña.delete('0', 'end')
			contracontraseña.configure(show="*")
	def out_contrasenacontra(*args):
	    if not contracontraseña.get():
	    	contracontraseña.insert(0,"Contraseña Nueva")
	    	contracontraseña.configure(show="")
	def in_contrasenacontran(*args):
		if not contranewcontraseña.get() or contranewcontraseña.get() == "Contraseña":
			contranewcontraseña.delete('0', 'end')
			contranewcontraseña.configure(show="*")
	def out_contrasenacontran(*args):
	    if not contranewcontraseña.get():
	    	contranewcontraseña.insert(0,"Contraseña")
	    	contranewcontraseña.configure(show="")
	login.withdraw()
	contra = Toplevel(); contra.title("Cambiar contraseña"); contra.geometry("340x220")
	gifreg = gif.init(contra, "../Project/Supplies/VentanaRegistro", delay=.2)
	contra.resizable(width=False, height=False);
	contrausuario       = Entry(contra, justify="center", bg="black", foreground="white"); contrausuario.place(x=40, y=130)
	contracontraseña    = Entry(contra, justify="center", bg="black", foreground="white"); contracontraseña.place(x=40, y=160)
	contranewcontraseña = Entry(contra, justify="center", bg="black", foreground="white"); contranewcontraseña.place(x=180, y=160)
	contraoksesion      = Button(contra, text="Iniciar sesión", command=lambda e=2: registrar(e), bg="black", foreground="white"); contraoksesion.place(x=130, y=190)
	contrausuario.insert(0,"Usuario"); contracontraseña.insert(0,"Contraseña Antigua"); contranewcontraseña.insert(0,"Contraseña Nueva")
	contrausuario.bind("<FocusIn>", in_usuariocontra); contrausuario.bind("<FocusOut>", out_usuariocontra)
	contracontraseña.bind("<FocusIn>", in_contrasenacontra); contracontraseña.bind("<FocusOut>", out_contrasenacontra)
	contranewcontraseña.bind("<FocusIn>", in_contrasenacontran); contranewcontraseña.bind("<FocusOut>", out_contrasenacontran)
	contra.protocol('WM_DELETE_WINDOW', lambda a=2: salir4(a))
	gifreg.hilo.start()
#Función para iniciar sesión
def iniciar():
	global usuarios; rjson()
	try:
		if encryp(usuario.get()) in usuarios:
			if usuarios[encryp(usuario.get())][0] == encryp(contraseña.get()):
				juegos()
			else:
				messagebox.showerror("Error","Contraseña incorrecta, intente de nuevo.")
		else:
			messagebox.showwarning("Usuario inexistente","El usuario " + usuario.get() + " no existe, regístrese primero.")
	except: print("")
#Función para que aparezca la ventana de iniciar sesión
def loginv():
	global usuarios, usuario, contraseña, gif2, login
	login.deiconify()
	gif2       = gif.init(login,"../Project/Supplies/VentanaSesion", delay=.12); gif2.hilo.start()
	menusesion = Menu(login); login.config(menu=menusesion)
	usuario    = Entry(login, justify="center", foreground="white", bg="black"); usuario.place(x=70, y=310)
	contraseña = Entry(login, justify="center", foreground="white", bg="black"); contraseña.place(x=210, y=310)
	oksesion   = Button(login, text="Iniciar sesión", justify="center", command=iniciar, foreground="white", bg="black"); oksesion.place(x=350, y=310)
	usuario.insert(0,"Usuario"); contraseña.insert(0,"Contraseña")
	usuario.bind("<FocusIn>", in_usuario); usuario.bind("<FocusOut>", out_usuario)
	contraseña.bind("<FocusIn>", in_contrasena); contraseña.bind("<FocusOut>", out_contrasena)
	menusesion.add_command(label='Registro',command=registro)
	menusesion.add_command(label='Cambiar contraseña',command=contrasena)
#Inicia la pantalla para escoger juegos
def juegos():
	global prdos, concntrc, gif1, gif2, usuario
	ventana.deiconify(); login.withdraw(); gif2.hilo.stopgif(); 
	gif1 = gif.init(ventana,"../Project/Supplies/VentanaGames", delay=.02); gif1.hilo.start()
	G1   = Button(ventana, command=game1, image=prdos[0])
	G2   = Button(ventana, command=game2, image=concntrc[0][0])
	G1.place(x=60, y=53); G2.place(x=280, y=53)
	menu = Menu(ventana); ventana.config(menu=menu)
	menu.add_command(label='Como jugar',command=comojugar)
#Cargar preguntas juego1
def cargarpreguntas(nivel):
	try:
		archivo = '../Project/Supplies/Nivel' + str(nivel) + '.csv'
		with open(archivo, newline='') as File:  
			reader = csv.reader(File, delimiter=',', quotechar='|')
			matriz = []
			for row in reader:
				matriz.append(row)
		return matriz
	except: 
		messagebox.showerror("Error", "No existe archivo de preguntas")
#Cargar imagenes
def cargar():
	global A, prdos, concntrc, fondos, htp
	z1, z2, z3, z4 = [], [], [], []
	htp   = PhotoImage(file="../Project/Supplies/VentanaInstrucciones/int.png")
	prdos = [PhotoImage(file="../Project/Supplies/Preguntados/"+file) for file in sorted(os.listdir("../Project/Supplies/Preguntados"))]	
	c0    = [PhotoImage(file="../Project/Supplies/Concentrese/Concentrese/"+file) for file in sorted(os.listdir("../Project/Supplies/Concentrese/Concentrese"))]	
	c1    = [PhotoImage(file="../Project/Supplies/Concentrese/Nivel1/"+file) for file in sorted(os.listdir("../Project/Supplies/Concentrese/Nivel1"))]
	c2    = [PhotoImage(file="../Project/Supplies/Concentrese/Nivel2/"+file) for file in sorted(os.listdir("../Project/Supplies/Concentrese/Nivel2"))]
	c3    = [PhotoImage(file="../Project/Supplies/Concentrese/Nivel3/"+file) for file in sorted(os.listdir("../Project/Supplies/Concentrese/Nivel3"))]
	d1    = [PhotoImage(file="../Project/Supplies/Concentrese/Fondo1/"+file) for file in sorted(os.listdir("../Project/Supplies/Concentrese/Fondo1"))]
	d2    = [PhotoImage(file="../Project/Supplies/Concentrese/Fondo2/"+file) for file in sorted(os.listdir("../Project/Supplies/Concentrese/Fondo2"))]
	concntrc = [c0, c1, c2, c3]; fondos = [d1, d2, d2]
#Inicia el juego #1
def game1():
	global usuarios, usuario, Game1, prdos, lvl
	ventana.withdraw()
	Game1 = Toplevel(); Game1.title("Bienvenido a Preguntados...")
	Game1.resizable(width=False, height=False);
	Game1.protocol('WM_DELETE_WINDOW',salir1); Game1.geometry("515x253")
	Label(Game1,image=prdos[1]).place(x=0, y=0)
	lvl1 = Button(Game1, text="Nivel 1", command=lambda x=1:levels1(x), image=prdos[2]); lvl1.place(x=20, y=20)
	lvl2 = Button(Game1, text="Nivel 2", command=lambda x=2:levels1(x), image=prdos[3]); lvl2.place(x=20, y=135)
	lvl3 = Button(Game1, text="Nivel 3", command=lambda x=3:levels1(x), image=prdos[4]); lvl3.place(x=390, y=85)
	lvl  = [lvl1, lvl2, lvl3];
	if usuarios[encryp(usuario.get())][2] == 1:
		lvl[1].configure(state=DISABLED)
		lvl[2].configure(state=DISABLED)
	if usuarios[encryp(usuario.get())][2] == 2:
		lvl[2].configure(state=DISABLED)
#Niveles del Juego 1
def levels1(a):
	global usuarios, usuario, Puntos, prdos, orden, counter, GL, P, Q
	Game1.withdraw(); questions = cargarpreguntas(a);
	orden = [(x*2) for x in range(10)]; shuffle(orden)
	GL    = Toplevel(); GL.title("Niveles..."); GL.geometry("600x360")
	GL.resizable(width=False, height=False);
	GL.protocol('WM_DELETE_WINDOW', salir5); contadorpreguntas = 0
	if a == 1:
		Label(GL, image=prdos[5]).place(x=0, y=0)
		Label(GL, text="Puntaje:").place(x=270, y=20)
	elif a == 2:
		Label(GL, image=prdos[6]).place(x=0, y=0)
		Label(GL, text="Puntaje:").place(x=270, y=20)
	else: 
		Label(GL, image=prdos[7]).place(x=0, y=0)
		Label(GL, text="Puntaje:").place(x=270, y=20)
	Puntos = Label(GL, text=usuarios[encryp(usuario.get())][1], width=5, justify="center");
	P      = Label(GL, text=questions[orden[0]][0]); P.place(x=50, y=80)
	Q      = [Button(GL,text=questions[orden[0]+1][i], command=lambda x=i, y=a: respuestas(contadorpreguntas,x,y,[])) for i in range(4)]
	[Q[i].place(x=50, y=140+30*i) for i in range(4)]; counter = clocktime(GL, 20,20)
	Puntos.place(x=350, y=20)
#Función que comprueba si es verdadera o falsa la respuesta
def respuestas(contadorpreguntas, i, nivel, correctas):
	global usuarios, usuario, counter, Puntos, orden, lvl, GL, P, Q
	questions = cargarpreguntas(nivel); contadorpreguntas += 1
	if contadorpreguntas < 10:
		contadorpreguntas -= 1
		if Q[i].cget('text') == questions[orden[contadorpreguntas]][1]:
			counter.hilo.stoptime(nivel, True); correctas.append(1)
		else: 
			counter.hilo.stoptime(nivel, False); correctas.append(0)
		contadorpreguntas += 1
		Puntos.configure(text=usuarios[encryp(usuario.get())][1])
		P.configure(text=questions[orden[contadorpreguntas]][0])
		ordeni = [i for i in range(4)]; shuffle(ordeni); shuffle(ordeni); shuffle(ordeni)
		[Q[i].configure(text=questions[orden[contadorpreguntas]+1][ordeni[i]], command=lambda x=i, y=nivel: respuestas(contadorpreguntas,x,y, correctas)) for i in range(4)]
		counter = clocktime(GL, 20, 20)
	else: 
		counter.hilo.stoptime(nivel, "")
		GL.destroy(); Game1.deiconify()
		if nivel == 1:
			if sum(correctas) > 5:
				lvl[1].configure(state=NORMAL); usuarios[encryp(usuario.get())][2] = 2; wjson(usuarios)
				messagebox.showinfo("Felicidades", "¡¡ Terminaste el nivel "+str(nivel)+"!!\nContinua al siguiente nivel")
			else:
				messagebox.showerror("Perdiste", "Tristemente perdiste este nivel, vuelve a iniciarlo")
		elif nivel == 2:
			if sum(correctas) > 7:
				lvl[2].configure(state=NORMAL); usuarios[encryp(usuario.get())][2] = 3; wjson(usuarios)
				messagebox.showinfo("Felicidades", "¡¡ Terminaste el nivel "+str(nivel)+"!!\nContinua al siguiente nivel")
			else:
				messagebox.showerror("Perdiste", "Tristemente perdiste este nivel, vuelve a iniciarlo")
		elif nivel == 3:
			if sum(correctas) > 9:
				messagebox.showinfo("Felicidades","Acabaste todos los niveles, puedes jugar en cualquier nivel que escojas")
			else:
				messagebox.showerror("Perdiste","Tristemente perdiste este nivel, vuelve a iniciarlo")
#Inicia el juego #2
def game2():
	global usuario, Game2, concntrc, lvl2
	ventana.withdraw()
	Game2 = Toplevel(); Game2.title("Bienvenido a Concentrese")
	Game2.resizable(width=False, height=False); Game2.geometry("605x405")
	Game2.protocol('WM_DELETE_WINDOW',salir2)
	Label(Game2, image=concntrc[0][1]).place(x=0, y=0)
	M1 = [0, 0, 0, 1, 1, 1, 2, 2, 2]; shuffle(M1); M1 = reshape(M1, (3,3))
	M2 = [0, 0, 0, 1, 1, 1, 2, 2, 2, 3, 3, 3, 4, 4, 4, 5]; shuffle(M2); M2 = reshape(M2, (4,4))
	M3 = [0, 0, 0, 1, 1, 1, 2, 2, 2, 3, 3, 3, 4, 4, 4, 5, 5, 5, 6, 6, 6, 7, 7, 7, 8]; 
	shuffle(M3); M3 = reshape(M3, (5, 5))
	lvl1 = Button(Game2, text="Nivel 1", image=concntrc[0][2], command=lambda x=1:levels2(x, M1, 3)); lvl1.place(x=40, y=180)
	lvl2 = Button(Game2, text="Nivel 2", image=concntrc[0][3], command=lambda x=2:levels2(x, M2, 4)); lvl2.place(x=140, y=230)
	lvl3 = Button(Game2, text="Nivel 3", image=concntrc[0][4], command=lambda x=3:levels2(x, M3, 5)); lvl3.place(x=240, y=280)
	lvl2  = [lvl1, lvl2, lvl3]
	if usuarios[encryp(usuario.get())][3] == 1:
		lvl2[1].configure(state=DISABLED)
		lvl2[2].configure(state=DISABLED)
	if usuarios[encryp(usuario.get())][3] == 2:
		lvl2[2].configure(state=DISABLED)
#Niveles del Juego 2
def levels2(nivel, M, n):
	global Game2, fondos, lvl2, contadorconcen, Puntos, quien, fig, CN, x, z
	Game2.withdraw(); CN = Toplevel(); fig = []
	CN.title("Concentrese"); contadorconcen, quien, x, z = 0, [], [], []
	CN.resizable(width=False, height=False); CN.protocol('WM_DELETE_WINDOW', salir6)
	if nivel == 1:
		Label(CN, image=concntrc[0][5]).place(x=0, y=0)
		Puntos = Label(CN, text=usuarios[encryp(usuario.get())][1], width=5, justify="center")
		CN.geometry("732x500"); Puntos.place(x=20, y=20)
		for i in range(n):
			fig.append([])
			for j in range(n):
				fig[i].append(Button(CN, image=fondos[nivel-1], command=lambda a=M, b=i, c=j: comparar(b,c,a,nivel,n)))
				fig[i][j].place(x=30 + 110 * i, y =150 + 110 * j)
	if nivel == 2:
		Label(CN, image=concntrc[0][6]).place(x=0, y=0)
		Puntos = Label(CN, text=usuarios[encryp(usuario.get())][1], width=5, justify="center")
		CN.geometry("485x485"); Puntos.place(x=0, y=0)
		for i in range(n):
			fig.append([])
			for j in range(n):
				fig[i].append(Button(CN, image=fondos[nivel-1], command=lambda a=M, b=i, c=j: comparar(b,c,a,nivel,n)))
				fig[i][j].place(x=30 + 110 * i, y =30 + 110 * j)
	if nivel == 3:
		Label(CN, image=concntrc[0][7]).place(x=0, y=0)
		Puntos = Label(CN, text=usuarios[encryp(usuario.get())][1], width=5, justify="center");
		CN.geometry("605x605"); Puntos.place(x=0, y=0)
		for i in range(n):
			fig.append([])
			for j in range(n):
				fig[i].append(Button(CN, image=fondos[nivel-1], command=lambda a=M, b=i, c=j: comparar(b,c,a,nivel,n)))
				fig[i][j].place(x=30 + 110 * i, y=40 + 110 * j)
#Función que mira las posiciones
def comparar(i, j, M, nivel, n):
	global contadorconcen, usuarios, usuario, concntrc, Puntos, quien, fig, x, z, x1, x2, y1, y2
	contadorconcen += 1
	if contadorconcen == 4:
		for h in range(n):
			for k in range(n):
				if [h, k] not in x:
					fig[h][k].configure(command=lambda a=h, b=k, c=M: comparar(a, b, c, nivel, n))
					fig[h][k].configure(image=fondos[nivel-1])
		quien, contadorconcen = [], 1
	if contadorconcen == 1:
		quien.append(M[i][j]) 
		fig[i][j].configure(image=concntrc[nivel][M[i][j]], command=nada)
		x1 = i; y1 = j
	if contadorconcen == 2:
		quien.append(M[i][j]) 
		fig[i][j].configure(image=concntrc[nivel][M[i][j]], command=nada)
		x2 = i; y2 = j
	if contadorconcen == 3:
		quien.append(M[i][j])
		fig[x1][y1].configure(command=lambda a=x1, b=y1, c=M: comparar(a, b, c, nivel, n))
		fig[x2][y2].configure(command=lambda a=x2, b=y2, c=M: comparar(a, b, c, nivel, n))
		fig[i][j].configure(image=concntrc[nivel][M[i][j]])
		if quien[0] == quien[1] and quien[1] == quien[2]:
			fig[x1][y1].configure(command=nada)
			fig[x2][y2].configure(command=nada)
			fig[i][j].configure(command=nada)
			x.append([i, j]); x.append([x1, y1]); x.append([x2, y2])
			usuarios[encryp(usuario.get())][1] += 20
		else:
			usuarios[encryp(usuario.get())][1] -= 5
		if usuarios[encryp(usuario.get())][1] <= 0:
			usuarios[encryp(usuario.get())][1] = 0
		Puntos.configure(text=usuarios[encryp(usuario.get())][1])
		if len(x)/3 == len(concntrc[nivel]) and nivel == 1:
			CN.destroy(); Game2.deiconify()
			messagebox.showinfo("Felicidades", "Has concluido el nivel, pasa al nivel 2")
			usuarios[encryp(usuario.get())][3] = 2; lvl2[1].configure(state=NORMAL)
		if len(x)/3 == len(concntrc[nivel])-1 and nivel == 2:
			CN.destroy(); Game2.deiconify()
			messagebox.showinfo("Felicidades", "Has concluido el nivel, pasa al nivel 3")
			usuarios[encryp(usuario.get())][3] = 3; lvl2[2].configure(state=NORMAL)
		elif len(x)/3 == len(concntrc[nivel])-1 and nivel == 3:
			CN.destroy(); Game2.deiconify()
			messagebox.showinfo("Felicidades", "Has concluido todos los niveles, puedes jugar en cualquier nivel.")
		wjson(usuarios)
#Función para no hacer nada
def nada():
	pass
#Función como jugar
def comojugar():
	global htp
	H = Toplevel()
	Label(H,image=htp).pack()
#Creación de la ventana principal
ventana    = Tk(); ventana.geometry("503x284"); ventana.title("Bienvenidos...")
ventana.withdraw(); cargar()
ventana.resizable(width=False, height=False);
#Creación de la ventana de iniciar sesión
login      = Toplevel(); login.title("Inicie sesión"); login.geometry("500x345")
login.resizable(width=False, height=False);
#Crea el gif de la ventana de escoger juegos
gif2       = gif.init(login,"../Project/Supplies/VentanaSesion", delay=.12); gif2.hilo.start()
menusesion = Menu(login); login.config(menu=menusesion)
usuario    = Entry(login, justify="center", foreground="white", bg="black"); usuario.place(x=70, y=310)
contraseña = Entry(login, justify="center", foreground="white", bg="black"); contraseña.place(x=210, y=310)
oksesion   = Button(login, text="Iniciar sesión", justify="center", command=iniciar, foreground="white", bg="black"); oksesion.place(x=350, y=310)
usuario.insert(0,"Usuario"); contraseña.insert(0,"Contraseña")
usuario.bind("<FocusIn>", in_usuario); usuario.bind("<FocusOut>", out_usuario)
contraseña.bind("<FocusIn>", in_contrasena); contraseña.bind("<FocusOut>", out_contrasena)
menusesion.add_command(label='Registro',command=registro)
menusesion.add_command(label='Cambiar contraseña',command=contrasena)
ventana.protocol('WM_DELETE_WINDOW',salir3)
login.protocol('WM_DELETE_WINDOW',salir)

mainloop()
