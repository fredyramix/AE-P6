__author__ = 'freddy'
#Esta funcion recibe

def calcularAptitudPoblacion(poblacion,mA,mB,tamano):
    print mA
    print mB
    aptitudes = []
    for vector in poblacion:
        print vector

        sumatoria=0
        for i in range(0,tamano):
            for j in range(0,tamano):
                print "i: "+str(i)
                print "j: "+str(j)
                sumatoria=sumatoria+(mA[i][j] * mB[vector[i]][vector[j]])
                print sumatoria
            raw_input("esperaddd")
        aptitudes.append(sumatoria)
    return aptitudes

#Mejor solucion 1,816,000