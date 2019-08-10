"""
Antonio Villanueva Segura
Matriz Rusa  5x5 en python3 con clase ...
"""
#!/usr/bin/env python
# -*- coding: utf-8 -*-
from tkinter import *
import random

class Juego ():
	def __init__(self):
		"""constructor del Juego """
		self.matriz=[] #Estructura con numeros,activacion,seleccionado
		
		self.LabelIzq=[] #Etiquetas con el valor de la suma buscado
		self.LabelDer=[] #Etiquetas con el valor de la suma buscado	
		self.LabelSup=[] #Etiquetas con el valor de la suma buscado
		self.LabelInf=[] #Etiquetas con el valor de la suma buscado	
		
		self.intentos=0 #Intentos del jugador
		
		self.creaJuego() #Construye juego 	

	def botonFin(self,ventana):
		""" Fin de partida , destruye ventana e reinicializa el juego"""
		ventana.destroy()
		self. __init__()
		
	def callback(self,boton):
		"""Accion sobre el boton , lo desactiva para la suma """

		if (boton.cget('bg')=='red'):
			boton.configure(bg = 'yellow')
		else:
			boton.configure(bg = "red")

		self.intentos+=1
			
		if (self.analisisArray()):#Analiza sumas 
			print ("Lo has conseguido en ",self.intentos, "intentos")
			ventanaInformativa = Toplevel()
			ventanaInformativa.resizable(0,0) #No cambiar size ventana
			ventanaInformativa.geometry("300x50+0+0")
			Label(ventanaInformativa ,text="Ok lo has conseguido en  "+str(self.intentos),fg='red').pack()
			Button(ventanaInformativa ,text="OK",fg='red',command= lambda ventana=ventanaInformativa: self.botonFin(ventana)).pack()			

	def aleatorio(self,minimo=1,maximo=10):
		"""genera un numero aleatorio en rango max. num"""
		return random.randrange(minimo,maximo)
		
	def creaArray(self):
		"""crea un array 2D 5x5 Primer Campo es el boton, el segundo si es activo en el resultado suma"""		
		for x in range (0,5):
			linea=[]#Crea una linea vacia			
			for y in range(0,5):	
				linea.append( [ Button(root,text=str( self.aleatorio() ),bg="yellow"), #Crea un boton
								True if (self.aleatorio(0,2)==1) else False ] )
				#Configura el callback con el ultimo boton en si mismo
				linea[-1][0].configure(command= lambda boton=linea[-1][0]: self.callback(boton) ) 	
				linea[-1][0].grid(row=x+1, column=y+1)# Lo inserta graficamente en la rejilla	
										
			self.matriz.append(linea)#Anade  linea a la matriz 2D 

	def analisisArray(self):
		"""Analiza suma en las lineas """
		for x in range (0,5):#Recorre x lineas
			suma=0
			for y in range (0,5):#Recorre y  columnas
				
				if self.matriz[x][y][0].cget('bg')=='yellow':#Es un boton activo en la suma
					suma+=int (self.matriz[x][y][0].cget('text'))#Recupera cifra en el boton				
					
			""" Afecta color etiquetas Izq. y Der. """	
			if suma == int ( self.LabelIzq[x].cget('text') ):#Si la suma se cumple es verde
				self.LabelIzq[x].configure(fg='green')
				self.LabelDer[x].configure(fg='green')					
			else:
				self.LabelIzq[x].configure(fg='blue')
				self.LabelDer[x].configure(fg='blue')		
					
		"""Analiza suma en columnas """
		for y in range (0,5):#Recorre y lineas
			suma=0
			for x in range (0,5):#Recorre x  columnas
				
				if self.matriz[x][y][0].cget('bg')=='yellow':#Es un boton activo en la suma
					suma+=int (self.matriz[x][y][0].cget('text'))#Recupera cifra en el boton				
					
			""" Afecta color etiquetas Sup. e Inf. """	
			if suma ==  int ( self.LabelSup[y].cget('text') ):#Si la suma se cumple es verde

				self.LabelSup[y].configure(fg='green')
				self.LabelInf[y].configure(fg='green')					
			else:
				self.LabelSup[y].configure(fg='blue')
				self.LabelInf[y].configure(fg='blue')	


		"""Ha sido completada , las etiquetas son verdes """
		for etiqueta in self.LabelIzq:
			if etiqueta.cget('fg')=='blue':
				return False
				
		for etiqueta in self.LabelSup:
			if etiqueta.cget('fg')=='blue':
				return False	
		
		return True			
								
	def creaEtiquetasSuma(self):		
		""" crea las etiquetas laterales ,superior e inferior con la suma"""			
		for x in range (0,5):#Recorre x las lineas
			suma=0#Inicializa la suma 
			for y in range(0,5):#Crea la suma de esta linea
				if self.matriz[x][y][1]:#Es elemento de suma ?
					suma+= int (self.matriz[x][y][0].cget('text'))

			#Etiquetas en x, 0,1,2,3,4
			self.LabelIzq.append (Label(root,text=str(suma),fg='blue'))
			self.LabelIzq[-1].grid(row=x+1, column=0)#Coordenas 
			self.LabelDer.append (Label(root,text=str(suma),fg='blue'))	
			self.LabelDer[-1].grid(row=x+1, column=7)#Coordenas 
						
		"""Genera etiquetas columna de suma arriba e abajo """
		for y in range (0,5):#Recorre las columnas
			suma=0#Inicializa la suma 			
			for x in range(0,5):#Crea la suma de esta linea
				if self.matriz[x][y][1]:#Es elemento de suma ?
					suma+= int (self.matriz[x][y][0].cget('text'))
					
			#Etiquetas en y, 0,1,2,3,4		
			self.LabelSup.append (Label(root,text=str(suma),fg='blue'))
			self.LabelSup[-1].grid(row=0, column=y+1)#Coordenas 
			self.LabelInf.append (Label(root,text=str(suma),fg='blue'))
			self.LabelInf[-1].grid(row=7, column=y+1)#Coordenas 
							
	def creaJuego(self):
		""" Crea matriz 5x5 etiquetas y botones """
		self.creaArray()#Inicializa el array de numeros aleatorios de 3 campos
		#self.creaBotones() #Botones con los datos de la matriz
		self.creaEtiquetasSuma() #Labels laterales sup. e inf.


		#Debug para analizar las casillas seleccionadas 

		for x in range (5):
			for y in range (5):
				print (self.matriz[x][y][1], end=",")
			print ("\n")
			
root = Tk()
root.config(bd=5)  # borde exterior de la ventana 10 Pixels
root.title('5x5  A.Villanueva')
root.resizable(0,0) #No cambiar size ventana

matrizRusa=Juego() #Instancia el Juego 
root.mainloop()
