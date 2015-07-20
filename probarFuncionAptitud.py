__author__ = 'jramirez'
from funcionAptitud import calcularAptitudPoblacion

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