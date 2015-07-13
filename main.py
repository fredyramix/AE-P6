__author__ = 'freddy'
from os import listdir
from os.path import isfile, join
from funcionAptitud import *
from SeleccionarMejor import elitismo
from cruzamiento import cruzar
from seleccion import seleccionar
from penalizacion import penalizar

import random

MINIMIZACION = 1.0
MAXIMIZACION = -1.0
TAMANIO_POBLACION = 20
#TAMANIO_INDIVIDUO = 5
MAX_NUMERO_GENERACIONES = 1000

TIPO_PROBLEMA = MAXIMIZACION

def crearPoblacion(tamanioPoblacion, tamanioIndividuo):
    return [[random.randint(0,tamanioIndividuo-1) for i in range(tamanioIndividuo)] for j in range(tamanioPoblacion)]

def imprimirIndividuo(individuo, aptitud):
    print aptitud, individuo

def imprimirPoblacion(poblacion, aptitudes):
    for individuo, aptitud in zip(poblacion, aptitudes):
        imprimirIndividuo(individuo, aptitud)

def calcularAptitud(individuo):
    aptitud = 0.0
    for alelo in individuo:
        if alelo == 0:
            aptitud+=1.0
    return  aptitud*TIPO_PROBLEMA



def preSeleccion(aptitudes):
	totalAptitudes = sum(aptitudes)
	float(totalAptitudes)
	valoresEsperados = [float(aptitud)/totalAptitudes for aptitud in aptitudes]
	print valoresEsperados
	raw_input("espera")
	#print sum(valoresEsperados)
	return valoresEsperados

def seleccion(valoresEsperados):
	r = random.random()
	sve = 0.0
	for i, ve in zip(range(TAMANIO_POBLACION), valoresEsperados):
		sve += ve
		if r < sve:
			return i
	return TAMANIO_POBLACION-1


'''def cruzar(padre, madre):
	puntoCruza = random.randint(1, TAMANIO_INDIVIDUO-2)
	#print "Punto cruza: ", puntoCruza
	hijo1 = padre[:puntoCruza] + madre[puntoCruza:]
	hijo2 = madre[:puntoCruza] + padre[puntoCruza:]
	return hijo1, hijo2'''

def mutar(individuo):
	pm = 1.0 / TAMANIO_INDIVIDUO
	for i in range(TAMANIO_INDIVIDUO):
		r = random.random()
		if r < pm:
			if individuo[i] == 0:
				individuo[i] = 1
			else:
				individuo[i] = 0
	return individuo


def seleccionarMejores(poblacion):
	poblacionOrdenada = sorted(poblacion, key=calcularAptitud)
	return poblacionOrdenada[:TAMANIO_POBLACION]

def leerArchivos():
	dic={}
	for i,archivo in enumerate(listdir("archivos/")):
		print "["+str(i)+"]"+archivo
		dic[str(i)]=archivo
	opcion=raw_input()
	return opcion,dic

def openFileDat(opcion,dic):
	salida=[]
	fo = open("archivos/"+dic[opcion], "r")
	configuracion= [linea.split() for linea in fo.readlines()]
	fo.close()
	for i in configuracion:
		if i != []:
			salida.append(i)
	tamano = int(salida[0][0])
	del salida[0] #eliminamos el parametro del tamano
	mA= salida[:tamano]
	mB= salida[tamano:]
	for i in range(len(mA)):
		for j in range(len(mA)):
			mA[i][j]=int(j)
	for i in range(len(mB)):
		for j in range(len(mB)):
			mB[i][j]=int(j)
	return tamano,mA,mB

def main():
	mejor=[]
	mejor.append(-1)
	mejor.append(-1)
	print "Practica 6 multiplicacion de matrices:"
	print "Selecciona una opcion []:"
	opcion,dic=leerArchivos()
	TAMANIO_INDIVIDUO ,mA,mB=openFileDat(opcion,dic)
	poblacion = crearPoblacion(TAMANIO_POBLACION, TAMANIO_INDIVIDUO)
	aptitudes = calcularAptitudPoblacion(poblacion,mA,mB,TAMANIO_INDIVIDUO)
	mejor = elitismo(poblacion, aptitudes,mejor)
	print mejor
	while True:
		penalizados=penalizar(poblacion,aptitudes,TAMANIO_INDIVIDUO)
		seleccionados=seleccionar(poblacion,penalizados)
		raw_input("Hasta aqui voy")
		cruzados= cruzar(seleccionados)

	#imprimirPoblacion(poblacion, aptitudes)
	#for generacion in range(MAX_NUMERO_GENERACIONES):
	#	valoresEsperados = preSeleccion(aptitudes)
	#	raw_input("Hasta aqui voy....")
	#	for i in range(TAMANIO_POBLACION/2):
	'''		pos1 = seleccion(valoresEsperados)
			pos2 = seleccion(valoresEsperados)

			#print "Cruzar: ",pos1, pos2
			hijo1, hijo2 = cruzar(poblacion[pos1], poblacion[pos2])
			#imprimirIndividuo(hijo1, calcularAptitud(hijo1))
			#imprimirIndividuo(hijo2, calcularAptitud(hijo2))
			hijo1 = mutar(hijo1)
			hijo2 = mutar(hijo2)

			poblacion.append(hijo1)
			poblacion.append(hijo2)

		poblacion = seleccionarMejores(poblacion)
		aptitudes = calcularAptitudPoblacion(poblacion)
		print "Generacion ", generacion
		#imprimirPoblacion(poblacion, aptitudes)

		print 'El mejor:'
		imprimirIndividuo(elMejor[0], elMejor[1])

	print 'EL mejor de los mejores del universo:'
	imprimirIndividuo(elMejor[0], elMejor[1])'''


main()