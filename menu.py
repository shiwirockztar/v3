from	usuarios import Usuarios
from	bots import Bots
import sys          #libreria para limpiar pantalla
import time         #libreria para el uso del time.sleep()
import random       #libreria para el uso de los numero aleatorios
import os           #libreria para el uso del os.system('cls')

pista=random.randint(69, 100)

vs=[]

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
		print("la pista mide ",pista*100," mts")
		print()
		print(menu)
		op=op+1
		# op=int(input("Por favor introduzca la opcion a elegir\n"))
		if op==1:
# *********************** creacion de competidores *************************					
			x=Bots()
			print("--------- la partida cuenta con ",x.tamaño+1," carriles -----------")
# ************************ modificando carril repetido de 1 rival ************ 		
			y=Usuarios()
			x.setCarril(y.carril)

# ************************ modificando carril repetido de 1 rival ************ 
# *************** y aqui en la lista vs ya estan ordenados por orden de vias ************ 

			# vs=x.Import(y.conductor,y.carro,y.carril)
		
		elif op==2:
			# x.visual()
			# y.mostrar()
			for k in range(x.tamaño+1):
				x.enlist(k)
				y.enlist(k)
				pass
			
			pass
		elif op==3:
			for k in range(x.tamaño+1):
				x.play(k)
				y.play(k)
				pass
			pass
		elif op==4:
			jugar()

		elif op==6:
			break
			
		if op==9:
			buscar()

		os.system('pause')
		pass
		os.system('cls')
	pass


def creacion(tamaño):
	for x in range(tamaño):
		pass

def jugar():

	os.system('pause')	
	pass