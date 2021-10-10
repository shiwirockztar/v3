import sys          #libreria para limpiar pantalla
import time         #libreria para el uso del time.sleep()
import random       #libreria para el uso de los numero aleatorios
import os           #libreria para el uso del os.system('cls')

global lista
lista= list()
# listas ejemplos
cars=["redbull","lamborghini","ferrari","BMW","sauber","porsche","mclaren"]
drivs=["montoya","vettel","schumacher","hamilton","alonzo","speedy"]
Team=[]

class Bots:
	"""bots"""
	carro=""
	conductor=""
	carril=0
	tamaño=0
	# Team=[]

	def __init__(self,x):
		self.conductor=drivs[x]
		self.carro=cars[x]
		self.carril=x
		pass


	def rival(self,x):
		self.conductor=drivs[x]
		self.carro=cars[x]
		self.carril=x
		lista.append([self.conductor,self.carro,self.carril])
		print(lista)
		return self.conductor,self.carro,self.carril
		pass

	def creacion(self):

		pass


	def display(self):
		# print("este es la visual de datos")
		for x in Team:
			print("El jugador ",x[0]," juega con el carro ",x[1],"en el carril ",x[2])
			pass

		print("---------------   modo lista de objetos  ---------------")


		for a in lista:
			print("El jugador ",a.conductor," juega con el carro ",a.carro,"en el carril ",a.carril) 
			pass