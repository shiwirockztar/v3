import sys          #libreria para limpiar pantalla
import time         #libreria para el uso del time.sleep()
import random       #libreria para el uso de los numero aleatorios
import os           #libreria para el uso del os.system('cls')

global lista
lista= list()
# listas ejemplos
cars=["redbull","lamborghini","ferrari","BMW","sauber","porsche","mclaren"]
drivs=["montoya","vettel","schumacher","hamilton","alonzo","speedy"]
challengers=[]

# definimos los atributos
class Bots:
	"""bots"""
	carro=""
	conductor=""
	carril=0
	tamaño=0

	def __init__(self,x="default"):
		
		if x=="default":
			# print("inicializacion de challengers")
			self.rival()
			pass		
		if x!="default":
			self.conductor=drivs[x]
			self.carro=cars[x]
			self.carril=x			
			pass
		pass

	def rival(self):
		r=random.randint(2, 6)
		for x in range(r):
			t=Bots(x)
			challengers.append(t)
			pass
		pass

	def visual(self):
		print("imprimiendo x visual")
		for x in challengers:
			print("El conductor ",x.conductor," juega con el carro ",x.carro,"en el carril ",x.carril) 
			pass
		pass

# ________________________________ metodo para crear y mostrar de manera distinta______________________
# ---------------------------------------------- un grupo de objetos ----------------------------------
	def display(self):
		print("metodo display")
		r=random.randint(2, 6)
		objs = [Bots(i) for i in range(r)]
		for x in range(r):
			print("El conductor ",objs[x].conductor," juega con el carro ",objs[x].carro,"en el carril ",objs[x].carril) 
			pass
		pass





