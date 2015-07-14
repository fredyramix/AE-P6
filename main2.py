__author__ = 'freddy'
from os import listdir
from os.path import isfile, join
from funcionAptitud import *
from SeleccionarMejor import elitismo
from cruzamiento import cruzar
from seleccion import seleccionar
from penalizacion import penalizar
from mutacion import mutar
import random

MINIMIZACION = 1.0
MAXIMIZACION = -1.0
TAMANIO_POBLACION = 20
MAX_NUMERO_GENERACIONES = 1000

TIPO_PROBLEMA = MAXIMIZACION

def crearPoblacion(tamanioPoblacion, tamanioIndividuo):
	return [[random.randint(0,tamanioIndividuo-1) for i in range(tamanioIndividuo)] for j in range(tamanioPoblacion)]


def leerArchivos():
	dic={}
	for i,archivo in enumerate(listdir("archivos/")):
		print "["+str(i)+"]"+archivo
		dic[str(i)]=archivo
	opcion=raw_input("Ingresa una opcion:  ")
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
main()