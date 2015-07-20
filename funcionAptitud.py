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
def main():
    mA=[[0,5,2,4,1],[5,0,3,0,2],[2,3,0,0,0],[4,0,0,0,5],[1,2,0,5,0]]
    mB=[[0,1,1,2,3],[1,0,2,1,2],[1,2,0,1,2],[2,1,1,0,1],[3,2,2,1,0]]
    v=[[1,3,0,3,3]]
    tam=5

    aptitud=calcularAptitudPoblacion(v,mA,mB,tam)

    print "==========Matriz 1================="
    for fila in mA:
        print fila
    print "==========Matriz 2================="
    for fila in mB:
        print fila
    print "==========Vector================="
    print v
    print "==========Aptitud================="
    print aptitud

#main()