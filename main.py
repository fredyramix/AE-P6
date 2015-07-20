__author__='Freddy'

from os import listdir
from salida import escribir
#from os.path import isfile,join
from funcionAptitud import calcularAptitudPoblacion
from SeleccionarMejor import elitismo
from cruzamiento import *
from seleccion import seleccionar
from mutacion import mutar
import time
import itertools
from penalizacion import penalizar
import random

TAM_POBLACION=20
NUM_GENERACIONES=1000

def crearPoblacion(tamanioPoblacion, tamanioIndividuo):
	#primer paso crear una lista de posiciones
	return [[random.randint(0,tamanioIndividuo-1) for i in range(tamanioIndividuo)] for j in range(tamanioPoblacion)]
	'''lista_de_posiciones=[]
	poblacion=[]
	for i in range(0,tamanioIndividuo):
		lista_de_posiciones.append(i)
	a= list(itertools.permutations(lista_de_posiciones))
	b=a[:20]
	for cromosoma in (b):
		poblacion.append(list(cromosoma))
	return poblacion'''
	#############################################
	'''poblacion=[]
	lista=[]
	for i in range(0,tamanioIndividuo):
		lista.append(i)
	#print lista

	for j in range(0,tamanioPoblacion):
		lista_temporal=lista[:]
		random.shuffle(lista_temporal)
		poblacion.append(lista_temporal)
	return poblacion'''


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
	for i in range(0,len(mA)):
		for j in range(0,len(mA)):
			#print mA[i][j]
			mA[i][j]=int(mA[i][j])
	for i in range(0,len(mB)):
		for j in range(0,len(mB)):
			mB[i][j]=int(mB[i][j])
	return tamano,mA,mB
def main(start_time):
	outfile=open("Resultados/salida.txt",'w')
	mejor = []
	mejor.append(-1)
	mejor.append(-1)
	print "============Practica 6 Multiplicacion de matrices========"
	opcion,dic = leerArchivos()
	TAM_INDIVIDUO,mA,mB = openFileDat(opcion, dic)

	poblacion = crearPoblacion(TAM_POBLACION, TAM_INDIVIDUO)
	#for p in poblacion:
	#	print ps
	#raw_input("aaaaaaaaa")

	aptitudes = calcularAptitudPoblacion(poblacion, mA, mB, TAM_INDIVIDUO)

	aptitudes=penalizar(poblacion,aptitudes)

	mejor,b = elitismo(poblacion, aptitudes,mejor)
	a="El mejor hasta ahora:"
	escribir(outfile,a)
	a= "Generacion: " +str(0)
	escribir(outfile,a)
	a= "Vector: "+str(mejor[0])
	escribir(outfile,a)
	a="Aptitud: "+str(mejor[1])
	escribir(outfile,a)
	a="Tiempo: " +str(time.time()-start_time)+" segundos"
	escribir(outfile,a)
	g=0
	#while g != NUM_GENERACIONES:
	while True:
		#funcion de seleccion.
		#seleccionados=seleccionar(poblacion,aptitudes)
		#Cruzar a los seleccionados
		#cruza = cruzar(seleccionados)

		cruzados = cruzar(poblacion)

		#apti = calcularAptitudPoblacion(cruza, mA, mB, TAM_INDIVIDUO)

		#cruzados = seleccionarMejorCruza(apti,cruza)


		#cruzados = 0

		#hacer una mutacion
		poblacion=mutar(cruzados,TAM_INDIVIDUO)
		#calcular nueva aptitud
		aptitudes = calcularAptitudPoblacion(poblacion, mA, mB, TAM_INDIVIDUO)

		aptitudes=penalizar(poblacion,aptitudes)

		mejor,bandera = elitismo(poblacion, aptitudes,mejor)
		if mejor[1]==0:
			break
		else:
			if bandera==True:
				a="El mejor hasta ahora:"
				escribir(outfile,a)
				a= "Generacion: " +str(g)
				escribir(outfile,a)
				a= "Vector: "+str(mejor[0])
				escribir(outfile,a)
				a="Aptitud: "+str(mejor[1])
				escribir(outfile,a)
				a="Tiempo: " +str(time.time()-start_time)+" segundos"
				escribir(outfile,a)
		'''if g%100==0:
			a="El mejor hasta ahora:"
			escribir(outfile,a)
			a= "Generacion: " +str(g)
			escribir(outfile,a)
			a= "Vector: "+str(mejor[0])
			escribir(outfile,a)
			a="Aptitud: "+str(mejor[1])
			escribir(outfile,a)
			a="Tiempo: " +str(time.time()-start_time)+" segundos"
			escribir(outfile,a)
			a="=========================================================ss"
			escribir(outfile,a)'''
		g+=1
	a= "Termino en la generacion: " +str(g)
	escribir(outfile,a)
	a= "Vector: "+str(mejor[0])
	escribir(outfile,a)
	a= "Aptitud: "+str(mejor[1])
	escribir(outfile,a)
	a="Tiempo: " +str(time.time()-start_time)+" segundos"
	escribir(outfile,a)
	outfile.close()
	return 0

start_time = time.time()
main(start_time)