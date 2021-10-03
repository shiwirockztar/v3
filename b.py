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
class Team:
	carro=""
	conductor=""
	carril=0
	usuario=True

	def __init__(self,usuario=True,carro="",conductor="",carril=0):
		if usuario:
			print("creando equipo")	
			self.conductor=input("Por favor introduzca su nombre a elegir\n")
			self.carro=input("Por favor introduzca el equipo de escuderia\n")
			self.carril=int(input("Por favor introduzca la posiciona o carril a elegir\n"))
			self.usuario=False

		else:
			self.conductor=c
			self.carro=ca
			self.carril=cr
		pass

	def rival(self):
		r=random.randint(2, 6)
		print(r)
		for x in range(r):
			self.conductor=drivs[x]
			self.carro=cars[x]
			self.carril=x
			lista.append([self.conductor,self.carro,self.carril]) 
			pass
		pass
