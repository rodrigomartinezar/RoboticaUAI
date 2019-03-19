'''
Función que hace los calculos matriciales y retorna la solucion
'''
def matrixCalculation(displacement, rotation, x, y):
	import numpy as np
	import math as mt
	radians = mt.radians(rotation)
	matrixT = ([mt.cos(radians), -(mt.sin(radians)), 0, displacement[0]],
		 [mt.sin(radians), mt.cos(radians), 0, displacement[1]],
		 [0, 0, 1, displacement[2]],
		 [0, 0, 0, 1])
	print("Transformada: ")
	print(matrixT)
	matrixP = ([x],
		 	   [y],
			   [0],
		 	   [1])
	mt = np.matrix(matrixT)
	mp = np.matrix(matrixP)
	solution = np.matmul(mt , mp)
	return solution

'''
Función que hace plot de triangulo original segun su centroide
El plot siempre es el mismo. Solo varía segun el centroide que el usuario asigna
'''
def triangle(x, y):
	coordinates = []
	xCoordinates = []
	yCoordinates = []
	xCoordinates.append(x-2)
	xCoordinates.append(x)
	xCoordinates.append(x+2)
	yCoordinates.append(y-2)
	yCoordinates.append(y+2)
	yCoordinates.append(y)
	import matplotlib.pyplot as plt
	fig = plt.figure()
	plt.plot(xCoordinates, yCoordinates, marker='o', linestyle='-', c='b')
	plt.plot([xCoordinates[2], xCoordinates[0]],[yCoordinates[2], yCoordinates[0]], marker='o', linestyle='-', c='b')
	plt.plot(x,y,marker='o', c='r')
	plt.grid()
	plt.show()
	coordinates.append(xCoordinates)
	coordinates.append(yCoordinates)
	print(coordinates)
	return coordinates

'''
Función que hace plot del nuevo triangulo
'''
def newTriangle(x, y):
	import matplotlib.pyplot as plt
	fig = plt.figure()
	plt.plot(x, y, marker='o', linestyle='-', c='b')
	plt.plot([x[2], x[0]],[y[2], y[0]], marker='o', linestyle='-', c='b')
	plt.plot(0,0,marker='o', c='r')
	plt.grid()
	plt.show()

x = int(input("Ingresar coordenada x de centroide: "))
y = int(input("Ingresar coordenada y de centroide: "))
coordinatesOg = triangle(x, y)  #plot de triangulo original
print(coordinatesOg[0][0])
displacement = []
counter = 0
print("Ingrese desplazamiento en coordenada X, Y y Z")
while counter < 3:
	if counter == 0:
		displacement.append(int(input("Desplazamiento en X: ")))
	if counter == 1:
		displacement.append(int(input("Desplazamiento en Y: ")))
	if counter == 2:
		displacement.append(int(input("Desplazamiento en Z: ")))
	counter += 1
rotation = int(input("Ingrese grados de rotación: "))
correctAnswer = 0
if rotation != 0:
	while correctAnswer == 0:
		sentido = input("Derecha o Izquierda?: D o I  ")
		if sentido == 'D' or sentido == 'd':
			rotation = -(rotation)
			correctAnswer = 1
		elif sentido == 'I' or sentido == 'i':
			correctAnswer = 1
		else:
			print("Respuesta no válida")
vertices = len(coordinatesOg[0])
verticesCounter = 0
newXcoordinates = []
newYcoordinates = []
while verticesCounter < 3:
	newPoint = matrixCalculation(displacement, rotation, coordinatesOg[0][verticesCounter], coordinatesOg[1][verticesCounter])
	newXcoordinates.append(float(newPoint[0]))
	newYcoordinates.append(float(newPoint[1]))
	verticesCounter += 1	
newTriangle(newXcoordinates, newYcoordinates)