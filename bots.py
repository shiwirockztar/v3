import sys          #libreria para limpiar pantalla
import time         #libreria para el uso del time.sleep()
import random       #libreria para el uso de los numero aleatorios
import os           #libreria para el uso del os.system('cls')

global lista
lista= list()
# listas ejemplos
cars=["redbull","lamborghini","ferrari","BMW","sauber","porsche","mclaren"]
drivs=["montoya","vettel","schumacher","hamilton","alonzo","speedy"]
vs=[]

class Bots:
	"""bots"""
	tamaño=0

	def __init__(self):
		r=random.randint(2, 6)
		print("el numero de jugadores es ",r)
		self.tamaño=r
		for x in range(r):
			self.conductor=drivs[x]
			self.carro=cars[x]
			self.carril=x
			vs.append([self.conductor,self.carro,self.carril]) 
			pass

		# a.conductor

	def rival(self):
		pass

	def creacion():
		pass

	def visual(self):

		# for x in range(self.tamaño):
		for x in vs:
			print("el conductor ",vs[x][0]," conduce con el carro ",vs[x][1])
			pass
		pass