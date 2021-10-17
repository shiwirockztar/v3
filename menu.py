from	usuarios import Usuarios
from	bots import Bots
import sys          #libreria para limpiar pantalla
import time         #libreria para el uso del time.sleep()
import random       #libreria para el uso de los numero aleatorios
import os           #libreria para el uso del os.system('cls')

carril=[0,1,2,3,4,5]
menu = """
====================================================
                         Menu
____________________________________________________
1.|               Registrar jugador
2.|               Mostrar competidores
3.|               Jugar
____________________________________________________
4.|               Salir
____________________________________________________
         """

def Menu():
	op=0
	while True:
		print(menu)
		op=int(input("Por favor introduzca la opcion a elegir\n"))
		if op==1:
			x=Usuarios()
			# print("el carril elegido fue ",x.carril)
			y=Bots()
			# z=Bots()
			# z.rival()
		elif op==2:
			x.mostrar()
			# y.display()
			y.visual()
			
		elif op==3:
			jugar()

		elif op==4:
			break
			
		if op==9:
			buscar()

		os.system('pause')
		pass
		os.system('cls')
	pass