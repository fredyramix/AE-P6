'''__author__ = 'freddy'
import random
def mutar(cruzados,tam):
    #print "Tamano de Poblacion: "+str(len(cruzados))
    x = random.randint(0,len(cruzados)-1)
    #print "numero de invididuo: "+str(x)
    muta= cruzados[x]
    #print "Individuo: "+str(muta)
    y = random.randint(0,len(muta)-1)
    #print "posicion individuo: "+str(y)
    #print "el que se va a mutar: "+str(muta[y])
    #print "Tamano Individuo: "+str(tam)
    w=random.randint(0,len(cruzados)-1)
    muta2= cruzados[w]
    z = random.randint(0,len(muta2)-1)

    #print "Nuevo numero:" +str(mut)
    a=cruzados[x][y]
    b=cruzados[w][z]

    cruzados[x][y]=b
    cruzados[w][z]=a
    #print cruzados
    return cruzados
    #raw_input("Aqui voy ")'''

__author__ = 'freddy'
import random
def mutar(cruzados,tam):
    #print "Tamano de Poblacion: "+str(len(cruzados))
    x = random.randint(0,len(cruzados)-1)
    #print "numero de invididuo: "+str(x)
    muta= cruzados[x]
    #print "Individuo: "+str(muta)
    y = random.randint(0,len(muta)-1)
    #print "posicion individuo: "+str(y)
    #print "el que se va a mutar: "+str(muta[y])
    #print "Tamano Individuo: "+str(tam)
    mut = random.randint(0,tam-1)
    #print "Nuevo numero:" +str(mut)
    cruzados[x][y]=mut
    #print cruzados
    return cruzados
    #raw_input("Aqui voy ")
