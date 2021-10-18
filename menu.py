from	usuarios import Usuarios
from	bots import Bots
import sys          #libreria para limpiar pantalla
import time         #libreria para el uso del time.sleep()
import random       #libreria para el uso de los numero aleatorios
import os           #libreria para el uso del os.system('cls')

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
		print(menu)
		op=int(input("Por favor introduzca la opcion a elegir\n"))
		if op==1:
# *********************** creacion de competidores *************************					
			x=Bots()
			print("--------- la partida cuenta con ",x.tamaño+1," carriles -----------")
			y=Usuarios()
# ************************ modificando carril repetido de 1 rival ************ 		

			x.setCarril(y.carril)

# ************************ modificando carril repetido de 1 rival ************ 
			vs=x.Import(y.conductor,y.carro,y.carril)
		
		elif op==2:
			print(vs)
			x.visual()
			y.mostrar()

			
			pass
		elif op==2:
			# mostrar()
			y.display()
			pass
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


def creacion(tamaño):
	
	for x in range(tamaño):

		# rivals.append(a)

		pass