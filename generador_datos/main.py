# coding=UTF-8
# Importamos las librerías
import sys
import os
import math
import csv
import numpy as np
from itertools import groupby
from mpl_toolkits.mplot3d import axes3d
import matplotlib.pyplot as plt
from matplotlib import cm


# Función que permite reiniciar el programa 
def reiniciar():
    python = sys.executable
    os.execl(python, python, * sys.argv)


# Función de cálculo que genera valores según la formula de distribucion normal de Gauss dadas unas coordenadas.
def funcionGauss(a,s,x,y,mux,muy):
	f = (a / (math.sqrt(2.0 * math.pi) * s)) * math.exp(-(0.5 / (s ** 2)) * ((x - mux) ** 2.0 + (y - muy) ** 2.0))
	return f

# Función que lee el fichero de datos y pinta un mapa de contornos en 3D
def generarGrafico():	
	data = []
	try: 
		# Abrimos el fichero de datos generado 
		ficheroDatos = open('datos.csv') 
		csv_reader = csv.reader(ficheroDatos)
		next(csv_reader, None)  # Quitamos la cabecera con el nombre de las variables

		# Cargamos los datos del fichero línea a línea
		for line in csv_reader:
			data.append(map(float, line))

		# Procesamos los datos cargados y creamos los arrays pertinentes para generar el gráfico
		X, Z = [], []
		for x, g in groupby(data, key=lambda line: line[0]):
			X.append(x)
			Y = []
			new_Z = []
			for y, gg in groupby(g, key=lambda line: line[1]):
				Y.append(y)
				new_Z.append(list(gg)[-1][2])
			Z.append(new_Z)

		# Transformamos X, Y y Z en formato de array válido para el gráfico 
		X, Y = np.meshgrid(X, Y) 
		Z = np.array(Z) 

		# Instanciamos un gráfico 3d de contornos
		fig = plt.figure()
		ax = fig.gca(projection='3d')

		# Generamos la supercicie de datos con los valores de X, Y y Z
		ax.plot_surface(X, Y,  Z, rstride=1, cstride=1, alpha=0.3)

		# Generamos los gráficos de contorno para cada una de las coordenadas
		cset = ax.contour(X, Y, Z, zdir='z', offset=-50, cmap=cm.coolwarm)
		cset = ax.contour(X, Y, Z, zdir='x', offset=-100, cmap=cm.coolwarm)
		cset = ax.contour(X, Y, Z, zdir='y', offset=-100, cmap=cm.coolwarm)

		# Añadimos el nombre a cada coordenada del gráfico y su rango de valores 
		ax.set_xlabel('X')
		ax.set_xlim(-100, 1200)
		ax.set_ylabel('Y')
		ax.set_ylim(-100, 1200)
		ax.set_zlabel('Z')
		ax.set_zlim(-50, 130)

		# Pintamos el gráfico
		plt.show()	
	finally:
		# Cerramos el fichero
		ficheroDatos.close()
		
	

def generarDatos():
	# Factor de corrección para los valores generados para evitar que sean demasiado bajos
	factorCorreccion = 0.00001

	# Inicializamos las varianzas que marcarán la dispersión de los datos generados respecto a la localización de las medias 
	s1=100.0
	s2=130.0
	s3=60.0


	# Inicializamos las coordenadas donde se van a ubicar las medias 
	mu1x=250.0
	mu1y=250.0
	mu2x=550.0
	mu2y=850.0
	mu3x=830.0
	mu3y=300.0


	# Inicializamos las medias
	a1=11500.0
	a2=12000.0
	a3=15500.0


	# Abrimos el fichero csv o dat de datos (o lo creamos en su defecto). 
	# Formato dat -> visualización de datos con GNUPlot.
	# Formato csv -> tratamiento de datos con WEKA.
	ficheroDatosCSV = open('datos.csv', 'w')
	ficheroDatosDat = open('datos.dat', 'w')

	# Creamos la cabecera con los nombres de las variables
	ficheroDatosCSV.write("x"+","+"y"+","+"f"+"\n")
	
	# Bucles anidados que genera los datos y los escribe en los ficheros
	for i in range(0, 100,4):
	
		# Discretizamos los valores del eje x en porciones de 10 unidades
		x = 100.0 + i * 10.0

		for j in range(0, 100,4):

			# Discretizamos los valores del eje y en porciones de 10 unidades
			y = 100.0 + j * 10.0
		
			# Creamos 3 distribuiciones normales con las diferentes medias y varianzas y recogemos el resultado 
			f1 = funcionGauss(a1,s1,x,y,mu1x,mu1y)
			f2 = funcionGauss(a2,s2,x,y,mu2x,mu2y)
			f3 = funcionGauss(a3,s3,x,y,mu3x,mu3y)

			# Escribimos los valores en los diferentes ficheros  
			ficheroDatosCSV.write( str(x) + "," + str(y) + "," + str(f1 + f2 + f3  + factorCorreccion)+"\n")
			ficheroDatosDat.write( str(x) + " " + str(y) + " " + str(f1 + f2 + f3 + factorCorreccion)+"\n")


	# Cerramos el fichero csv y dat
	ficheroDatosCSV.close()
	ficheroDatosDat.close()


		
def main():
	# Generamos los datos de ejemplo
	generarDatos()

	# Creamos el gráfico de superficie con los datos generados
	generarGrafico()


if __name__ == "__main__":
	main()
