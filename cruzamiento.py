__author__ = 'freddy'


def cruzar(poblacion):
    cruzados=[]
    print "========================================"
    for p in poblacion:
        print p
    n=len(poblacion[0])/2
    if n%2==0:
        n2=n
        pass#es par
    else:
        #Es un impar
        n2=n-1
    try:
        for i in range(0,len(poblacion)):
            ind1=poblacion[i][:n]
            ind2=poblacion[i][n:]
            ind3=poblacion[i+1][:n]
            ind4=poblacion[i+1][n:]
            ind5=ind1+ind4
            ind6=ind3+ind2
            cruzados.append(ind5)
            cruzados.append(ind6)
    except IndexError:
        pass
    print cruzados
    return cruzados
