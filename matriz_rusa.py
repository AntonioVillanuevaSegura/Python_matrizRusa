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

def b():
	return 0

def aleatorio(num=10):
	"""genera un numero aleatorio en rango max. num"""
	return random.randrange(num)
	
def creaArray():
	"""crea un array 2 5x5 con los diferentes numeros"""
	matriz5x5=[] #Estructura 5x5
	
	for x in range (0,5):
		linea=[]#Crea una linea vacia
		
		for y in range(0,5):	
			#Genera un numero aleatorio y su validez de suma
			linea.append([aleatorio(),aleatorio(2)])
			
		matriz5x5.append(linea)#Anade otra columna a la matriz 2d
		
	return matriz5x5
			
matriz=creaArray() #Crea array con los numeros
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
for y in range (0,5):
	for x in range(0,5):
		boton=Button(root, text=str(matriz[x][y][0]), command=b)
		boton.grid(row=x+1, column=y+1)


root.mainloop()
