__author__ = 'freddy'


def elitismo(poblacion, aptitudes,mejor):
    bandera=False
    nuevo = []
    #Esa funcion nos regresa una lista y la primer posicion es el menor.
    l=sorted(range(len(aptitudes)),key=aptitudes.__getitem__)
    #entonces el mejor es:s
    mejor_vector=poblacion[l[0]]
    mejor_aptitud=aptitudes[l[0]]
    nuevo.append(mejor_vector)
    nuevo.append(mejor_aptitud)
    if mejor[1]<0:
        #si mejor es vacio agregamos el primero como mejor.
        mejor[0]=nuevo[0]
        mejor[1]=nuevo[1]
    else:
        if nuevo[1]<mejor[1]:
            mejor[0]=nuevo[0]
            mejor[1]=nuevo[1]
            bandera=True
    return mejor,bandera
##uvid - Command ?
