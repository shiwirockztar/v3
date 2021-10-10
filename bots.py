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
c=[]

# definimos los atributos
class Bots:
	"""bots"""
	carro=""
	conductor=""
	carril=0
	tamaño=0
	# Team=[]

	def __init__(self,x=9):
		
		if x==9:
			print("inicializacion de la clase")
			pass
		
		if x!=9:
			self.conductor=drivs[x]
			self.carro=cars[x]
			self.carril=x			
			pass

		pass

	def rival(self,x):
		pass

	def creacionx(self):
		c,r=creacion()
		print(r)
		for a in c:
			print("El jugador ",a.conductor," juega con el carro ",a.carro,"en el carril ",a.carril) 
			pass
		pass


	def display(self):
		pass

def creacion():
	r=random.randint(2, 6)
	print("el numero de rivales es ",r)
	for x in range(r):
		a=Bots(x)
		# los objetos (rivales) creados pasan a una lista
		challengers.append(a)
		lista.append(a)
		# return challengers,r		
		return lista,r		

		pass

def display():
	# print("este es la visual de datos")
	print(challengers)
	for a in list(challengers):
		print("El jugador ",a.conductor," juega con el carro ",a.carro,"en el carril ",a.carril) 
		pass

	# print("El jugador ",a.conductor," juega con el carro ",a.carro,"en el carril ",a.carril) 
