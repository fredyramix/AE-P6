def cruzar(poblacion):
    cruzados=[]
    n=len(poblacion[0])/2
    if n%2==0:
        pass
    else:
        n=n+1
    while len(poblacion)!=0:
        ind1=poblacion[0]
        ind2=poblacion[1]
        p1=ind1[0:n]
        p2=ind1[n:]
        p3=ind2[0:n]
        p4=ind2[n:]

        n1=p1+p4
        n2=p3+p2
        cruzados.append(n1)
        cruzados.append(n2)
        del poblacion[0]
        del poblacion[0]
    return cruzados

