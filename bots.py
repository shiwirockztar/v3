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
t=[]


# definimos los atributos
class Bots:
	"""bots"""
	
	carro=""
	conductor=""
	carril=0
	tamaño=0
	kms=0
	posicion=0
	track=[]
	pos=0

	def __init__(self,x="default"):
		
		if x=="default":
			# print("inicializacion de challengers")
			self.rival()
			pass		
		if x!="default":
			self.conductor=drivs[x]
			self.carro=cars[x]
			self.carril=x
			self.kms=0			
			pass
		pass

	def rival(self):
		r=random.randint(3, 6)
		self.tamaño=r
		self.pos=0
		# ------- aqui crea una lista desde 0 hasta el tamaño+1 ------
		self.track=list(range(self.tamaño+1))
	
		for x in range(r):
			t=Bots(x)
			challengers.append(t)
			pass

	def visual(self):
		for x in challengers:
			print("El conductor ",x.conductor," juega con el carro ",x.carro,"en el carril ",x.carril) 
			pass
		pass

	def setCarril(self,via):			
		for x in challengers:
			
			if x.carril==via:
				x.carril=self.tamaño
			pass
		pass

	def export(self):
		for x in challengers:
			lista.append([x.conductor,x.carro,x.carril])
			pass
		pass

# ------------- envia los objetos como una lista ---------------
	def Import(self,cnd,car,via):
		
		lista.append([cnd,car,via])
		self.export()
		# print(lista)
		for x in lista:
			self.track[x[2]]=x	
		print("el selftrack es ",self.track)
		return self.track
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

# ________________________________ metodo para ORGANIZAR una coleccion______________________
# ----------------------------------------------de un grupo de objetos ----------------------------------
	def enlist(self,k):
		for x in challengers:
			if k==x.carril:
				print("El conductor ",x.conductor," juega con el carro ",x.carro,"en el carril ",x.carril)
				pass
			pass
		pass

	def play(self,k):
		for x in challengers:
			if k==x.carril:
				x.kms+=random.randint(1, 6)
				self.podio(x.kms)
				print(x.conductor," por el carril ",x.carril," lleva ",x.kms," kms")
				pass
			pass		
		pass

	def podio(self,k):
		if (k>=self.tamaño):
			self.pos+=1
			self.posicion=self.pos
			pass
		pass

	def premiacion(self):
		pass




