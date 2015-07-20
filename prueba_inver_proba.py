#archivo para prueba de probabilidad inversa

#lista= [38,102,200,59,78]
lista=[8,21,42,12,16]

print lista
lista2=[]
for i in lista:
	lista2.append(100.0/float(i))

print lista2

total = sum(lista2)
nueva=[]
for i in lista2:
	nueva.append((i/total)*100)
print nueva
print sum(nueva)