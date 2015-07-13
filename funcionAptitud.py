__author__ = 'freddy'
#Esta funcion recibe

def calcularAptitudPoblacion(poblacion,mA,mB,tamano):
    aptitudes = []
    for vector in poblacion:
        sumatoria=0
        for i in range(0,tamano):
            for j in range(0,tamano):
                sumatoria=sumatoria+(mA[i][j] * mB[vector[i]][vector[j]])
        aptitudes.append(sumatoria)
    return aptitudes

#Mejor solucion 1,816,000