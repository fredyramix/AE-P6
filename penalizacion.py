def penalizar(poblacion,aptitudes):
	penota=100000
	repeticiones=0
	lista_de_penas=[]
	for i in poblacion:
		repeticiones=0
		for j in range(0,len(i)):
			x=i.count(j)
			if x!=1:
				repeticiones+=x
		lista_de_penas.append(repeticiones*penota)
	aptis=sumar_pena_aptitud(aptitudes, lista_de_penas)
	return aptis

def sumar_pena_aptitud(apti,penas):
	for i in range(0,len(apti)):
		apti[i]=apti[i]+penas[i]
	return apti