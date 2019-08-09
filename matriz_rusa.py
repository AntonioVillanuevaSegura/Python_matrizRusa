"""
Antonio Villanueva Segura
"""
#!/usr/bin/env python
# -*- coding: utf-8 -*-
from tkinter import *
import random

root = Tk()
root.config(bd=15)  # borde exterior de 15 píxeles, queda mejor
#cadre = Frame(fen, width =200, height =150, bg="light yellow")

GRIS="#d9d9d9" #Color de fondo por defecto
def callback(boton):
	"""Accion sobre el boton , lo desactiva para la suma """
	
	if (boton.cget('bg')=='red'):
		boton.configure(bg = GRIS)
	else:
		boton.configure(bg = "red")


def aleatorio(num=10):
	"""genera un numero aleatorio en rango max. num"""
	return random.randrange(num)
	
def creaArray():
	"""crea un array 2 5x5 con los diferentes numeros"""
	matriz5x5=[] #Estructura 5x5
	
	for x in range (0,5):
		linea=[]#Crea una linea vacia
		
		for y in range(0,5):	
			#Genera numeros aleatorios, su validez para la suma, y por defecto es activo True , suma en el resultado
			linea.append([aleatorio(),aleatorio(2),True])
			
		matriz5x5.append(linea)#Anade otra columna a la matriz 2d
		
	return matriz5x5

def analisisArray(matriz):
	"""Analiza la suma de lineas y columnas """
	sumaLinea=0
	ctrl=0
	for x in range (0,5):#Recorre x las lineas
		suma=0
		ctrl=0
		for y in range (0,5):#Recorre y las columnas
			if matriz[x][y][1]==1:
				sumaLinea+=matriz[x][y][0]
			if matriz[x][y][2]==True:
				ctrl+=matriz[x][y][0]				
				
				
		print ("suma ",sumaLinea," , ",ctrl)
				


def creaJuego():
	""" Crea matriz 5x5 etiquetas y botones """
	matriz=creaArray() #Crea el array 5x5 con los numeros activos para suma
	botones=[]

	for lineas in matriz:
		print (lineas) #Debug

	"""Genera etiquetas linea de suma  laterales"""
	for x in range (0,5):#Recorre x las lineas
		suma=0#Inicializa la suma 
		
		for y in range(0,5):#Crea la suma de esta linea
			if matriz[x][y][1]:#Es elemento de suma ?
				suma+= matriz[x][y][0]
				
		Label(root,text=str(suma)).grid(row=x+1, column=0)
		Label(root,text=str(suma)).grid(row=x+1, column=7)	
		
	"""Genera etiquetas columna de suma arriba e abajo """
	for y in range (0,5):#Recorre y las columnas
		suma=0#Inicializa la suma 
		
		for x in range(0,5):#Crea la suma de esta columna
			if matriz[x][y][1]:#Es elemento de suma ?
				suma+= matriz[x][y][0]
				
		Label(root,text=str(suma)).grid(row=0, column=y+1)
		Label(root,text=str(suma)).grid(row=7, column=y+1)		
		

	""" Genera Botones del Juego y lee la matriz"""
	for x in range (0,5):
		for y in range(0,5):

			botones.append(  Button(root, text=str(matriz[x][y][0]), command=lambda x=x,y=y: callback((x,y)) ) )		
			botones[-1].grid(row=x+1, column=y+1)# Lo inserta graficamente en la rejilla
			
			#Configura el callback con el boton eb si mismo
			botones[-1].configure(command= lambda boton=botones[-1]: callback(boton) ) 
	return matriz
	

""" crea el juego y retorna la matriz donde solo extraigo el primer campo """
matriz=creaJuego()
analisisArray(matriz)
root.mainloop()
