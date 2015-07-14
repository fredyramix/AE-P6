__author__ = 'freddy'
def penalizar(poblacion,aptitudes,n):
    penalizados=[]
    pena=1000000
    for individuo in poblacion:
        penita=0
        for cromosoma in individuo:
            if cromosoma<0:
                #penalizar
                penita=penita+pena
            elif cromosoma>n:
                penita=penita+pena
                #penalizar
            else:
                #no se penaliza
                penita=penita+0
        penalizados.append(penita)
    for i in range(0,len(penalizados)):
        penalizados[i]=penalizados[i]+aptitudes[i]
    return penalizados
