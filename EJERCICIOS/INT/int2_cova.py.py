# -*- coding: utf-8 -*-
"""
Created on Fri Nov 22 16:13:52 2019

@author: UO264117
"""
'''
----------TEORIA -----------------
-----Fórmulas de Newton Cotes

3.3.- COMPUESTAS
Formulas de Newton Cotes

trapecio compuesta: evalua la funcion en los dos extremos del intervalo
todos los puntos intermedios perteneces a la vez a dos intervalos, 
porque tiene un intervalo a la derecha y optro a la izda
Todos los puntos cumplen esto excetpo los extremos



Simpson
lo parto en n intervalos
ahora la separacion que hay entre los puntos es h=((b-a)2n) 
entonces la longityd del intervalo es 2h



Al contrario que en derivación numérica, las fórmulas 
de integración compuesta son estables, esto es,
 la disminución de h no hace aumentar el error.
 
no puedo disminuir el error de forma indefinida
Pero no pasa que al aumentar la h empiece al aumentar el error


3.4.- INTEGRACION DE ROMBERG
Se basa en la formula del trapecio compuesta combinada con 
la extrapolacion de Richardson

ahora intentamos encontrar formulas que te digan, y con esta formula
el valor que podriamos esperar no es mayor que esto



3.5 ADAPTATIVA
Se basa en la regla se Simpson
es integracion con h variable



el romber obtiene el mismo resultado en el mismo tiempo de ejecucion
'''


import numpy as N
import sympy as S
import numpy.linalg as LA
import scipy.integrate as sci
import matplotlib.pyplot as plt

x=S.symbols('x',real=True)
f1=S.sin(x)
i1=[0,5]

sol_exacta=S.integrate(f1,(x,0,S.pi))
sol_exacta_num=S.lambdify(x,sol_exacta,'numpy')
fn1=S.lambdify(x,f1,'numpy')


puntos=N.arange(3,100,2) #asi creamos el numero de elementos

#creamos  una lista vacia para trapecio y otra pra simpson
#y ahi voy a ir almacenando la solucion para cada i


trapecio=[]
simpson=[]

for i in range(len(puntos)):
    soporte=N.linspace(0,N.pi,puntos[i]) #ahi hacemos 
    y1=fn1(soporte)
    
    sol_trapecio=sci.trapz(y1,soporte) #aqui jay qye ponerle el soporte porque hay que dar el valor de la x (sobre lo que integra)
    #la y es os valores de la funcion en ese soporte
    sol_simpson=sci.simps(y1,soporte)
    trapecio.append(sol_trapecio)
    simpson.append(sol_simpson)


evalu=sol_exacta*N.ones(len(puntos))
plt.figure()
plt.plot(puntos,evalu,label='Exacta')
plt.plot(puntos,trapecio,label='Trapecio')
plt.plot(puntos,simpson,label='Simpson')

plt.grid()
plt.legend()




f2=1/(1+x**2)
i2=[0,S.pi]
f3=S.exp(-x**2)
i3=[0,4]
f4=S.sqrt(1+x**2)
i4=[-1,1]




funciones=[f1,f2,f3,f4]
Nfun=len(funciones)
intervalos=[i1,i2,i3,i4]
NPts=len(puntos)

exacta=N.zeros(Nfun)
NSimpson=N.zeros(NPts)
NTrapez=N.zeros(NPts)


for i in range(Nfun):
    exacta[i]=float(S.integrate(funciones[i],(x,*intervalos[i])))
    fnum=S.lambdify(x,funciones[i],'numpy')
    for j in range(NPts):
        pp=N.array(intervalos[i]).astype(float)
        xx=N.linspace(*pp,puntos[j])
        yy=fnum(xx)
        NSimpson[j]=sci.simps(yy,xx)
        NTrapez[j]=sci.trapz(yy,xx)
    plt.figure(i,figsize=(10,8))
    plt.subplot(2,2,i+1)
    plt.title('$'+S.latex(funciones[i]))
    plt.plot(puntos,exacta[i]*N.ones(NPts),label='exacta')

    plt.plot(puntos,NTrapez,label='simpson')
    plt.plot(puntos,NSimpson,label='trapez')
    plt.legend()
    plt.grid()

plt.show()























