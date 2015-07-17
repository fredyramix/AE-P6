__author__='Freddy'

from os import listdir
from salida import escribir
#from os.path import isfile,join
from funcionAptitud import calcularAptitudPoblacion
from SeleccionarMejor import elitismo
from cruzamiento import cruzar
#from seleccion import seleccionar
from mutacion import mutar
import time

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
	aptitudes = calcularAptitudPoblacion(poblacion, mA, mB, TAM_INDIVIDUO)

	print aptitudes
	raw_input("aaaaaaa")
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
			if mejor[1]==1816000 and opcion=='3':
				break
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

start_time = time.time()
main(start_time)