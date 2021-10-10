import sys          #libreria para limpiar pantalla
import time         #libreria para el uso del time.sleep()
import random       #libreria para el uso de los numero aleatorios
import os           #libreria para el uso del os.system('cls')

global lista
lista= list()
# listas ejemplos
cars=["redbull","lamborghini","ferrari","BMW","sauber","porsche","mclaren"]
drivs=["montoya","vettel","schumacher","hamilton","alonzo","speedy"]

# definimos los atributos
class Usuarios:
	"""usuario"""
	carro=""
	conductor=""
	carril=0
	
	# usuario=True

	def __init__(self):
		
		print("creando equipo")	
		self.conductor=input("Por favor introduzca su nombre a elegir\n")
		self.carro=input("Por favor introduzca el nombre de equipo o escuderia\n")
		self.carril=int(input("Por favor introduzca la posiciona o carril a elegir\n"))
		# self.usuario=False	
		pass

	def display(self):
		pass


	
