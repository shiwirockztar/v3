from	usuarios import Usuarios
from	bots import Bots
import sys          #libreria para limpiar pantalla
import time         #libreria para el uso del time.sleep()
import random       #libreria para el uso de los numero aleatorios
import os           #libreria para el uso del os.system('cls')

rivals=[]

def creacion():
	r=random.randint(2, 6)
	print("el numero de rivales es ",r)
	for x in range(r):
		a=Bots()
		# los objetos (rivales) creados pasan a una lista
		rivals.append(a)

		pass

def Menu():
	op=0
	salir=4
	while op!=salir:
		print("Menu")
		print("1.- Registrar jugador")
		print("2.- Mostrar competidores")
		print("3.- Jugar")
		print("4.- Salir")
		op=int(input("Por favor introduzca la opcion a elegir\n"))
		if op==1:
			x=Usuarios()
			creacion()
			pass
		elif op==2:
			# mostrar()
			y.display()
			pass
		elif op==3:
			jugar()
			pass
		elif op==4:
			salir()
			pass
		if op==9:
			buscar()
			pass

		pass
	pass