import sys          #libreria para limpiar pantalla
import time         #libreria para el uso del time.sleep()
import random       #libreria para el uso de los numero aleatorios
import os           #libreria para el uso del os.system('cls')

# definimos los atributos
class Usuarios:
	"""usuario"""
	carro=""
	conductor=""
	carril=0

	def __init__(self):
		
		print("creando equipo")	
		self.conductor=input("Por favor introduzca su nombre a elegir\n")
		self.carro=input("Por favor introduzca el nombre de equipo o escuderia\n")
		self.carril=int(input("Por favor introduzca la posiciona o carril a elegir\n"))	

		pass

	def mostrar(self):
		print("El jugador ",self.conductor," juega con el carro ",self.carro,"en el carril ",self.carril) 
		pass

	def jugar():
		players=random.randint(4, 6)
		pista=random.randint(69, 100)
		print("la pista mide ",pista*100," mts")
		os.system('pause')	
		pass


	
