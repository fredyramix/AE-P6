__author__='Freddy'

from os import listdir
#from os.path import isfile,join
from funcionAptitud import calcularAptitudPoblacion
from SeleccionarMejor import elitismo
from cruzamiento import cruzar
#from seleccion import seleccionar
from mutacion import mutar

import random

TAM_POBLACION=20
NUM_GENERACIONES=10000

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
	mejor = []
	mejor.append(-1)
	mejor.append(-1)
	print "============Practica 6 Multiplicacion de matrices========"
	opcion,dic = leerArchivos()
	TAM_INDIVIDUO,mA,mB = openFileDat(opcion, dic)
	poblacion = crearPoblacion(TAM_POBLACION, TAM_INDIVIDUO)
	'''for pob in poblacion:
		print pob'''
	aptitudes = calcularAptitudPoblacion(poblacion, mA, mB, TAM_INDIVIDUO)

	#print aptitudes
	mejor,b = elitismo(poblacion, aptitudes,mejor)
	#print mejor
	g=0
	while True:
		cruzados = cruzar(poblacion)
		'''for cruz in cruzados:
			print cruz
		print "============"'''
		poblacion=mutar(cruzados,TAM_INDIVIDUO)
		'''for pob in poblacion:
			print pob
		print "============"
		raw_input("Esperad")'''
		aptitudes = calcularAptitudPoblacion(poblacion, mA, mB, TAM_INDIVIDUO)
		#raw_input("aqui")
		mejor,bandera = elitismo(poblacion, aptitudes,mejor)
		if mejor[1]==0:
			break
		else:
			if bandera==True:
				print "El mejor hasta ahora:"
				print "Generacion: " +str(g)
				print "Vector: "+str(mejor[0])
				print "Aptitud: "+str(mejor[1])
		g+=1
	print "Termino en la generacion: " +str(g)
	print "Vector: "+str(mejor[0])
	print "Aptitud: "+str(mejor[1])


main()