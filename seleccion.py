__author__ = 'freddy'


def seleccionar(poblacion,aptitudes):
    #Seleccion por ruleta.
    totalaptitud=sum(aptitudes)
    print totalaptitud
    print "============"
    print aptitudes

    print "Probabilidad Real:"
    probabilidades_real=[(float(proba)/float(totalaptitud))*100for proba in aptitudes]
    print probabilidades_real

    probabilidades_inv=[totalaptitud-proba for proba in probabilidades_real]
    print probabilidades_inv

    raw_input("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa")


#def rouleta(probas):
