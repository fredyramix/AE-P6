__author__ = 'freddy'
import random

def calcularProbabilidad(ap):
	lista2=[]
	nueva=[]
	for i in ap:
		lista2.append(100.0/float(i))
	total=sum(lista2)
	for j in lista2:
		nueva.append((j/total)*100)
	#print sum(nueva)
	return nueva	



def generarRangos(aptis,pob):
	num=random.uniform(0,100)
	rangos=[]
	seleccionados=[]
	#saptis.sort()
	aux=0.0
	for j in aptis:
		rangos.append(aux+j)
		aux += j
	#for x in rangos:
	#	print " "+str(count) +" : "+str(x)
	#	count += 1
	i=0
	while len(seleccionados) !=20:
		try: 
			if num<=rangos[i]:
				seleccionados.append(pob[i])
				i=0
				num=random.uniform(0,100)
			else:
				#print num
				#print rangos[i]
				#raw_input("no")
				i += 1
		except IndexError:
			print "i: "+str(i)
			print "num: " + str(num)
			print "rango: " +str(rangos[-1])
			raw_input("espera tio")

	#for sel in seleccionados:
	#	print sel
	#raw_input("aaqui")

	return seleccionados





def seleccionar(poblacion,aptitudes):
	#total=sum(aptitudes)
	#count=0
	#for p in aptitudes:
	#	print " "+str(count) +" : "+str(p)
	#	count +=1
	#print "=================================="
	probabilidades=calcularProbabilidad(aptitudes)
	#raw_input("aqui")
	#inversas=calcularProbabilidadInversa(probabilidades)
	#seleccionados=ruleta(inversas,poblacion)
	#raw_input("Espera")
	seleccionados=generarRangos(probabilidades,poblacion)
	#for s in seleccionados:
	#	print s
	#raw_input("Aqui voy")
	return seleccionados
