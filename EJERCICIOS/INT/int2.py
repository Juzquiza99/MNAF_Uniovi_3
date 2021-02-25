# -*- coding: utf-8 -*-
'''
Created on Fri Nov 22 19:02:00 2019

@author: javie


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


import sympy as S
import numpy as N
import scipy.integrate as sc
import matplotlib.pyplot as plt

#Adaptativas
#EJEMPLO 9
x=S.symbols('x',real=True)
funciones=[S.sin(x),(1/(x**2 +1)),S.exp(-x**2),S.sqrt(x**2 +1)]
intervalos=[[0,N.pi],[0,5],[0,4],[-1,1]]

puntos=N.arange(3,100,2) #para tener impares y que no de problemas en simpson
nptos=len(puntos)
nfun=len(funciones)

exacta=N.zeros(nfun)
ntrap=N.zeros(nptos)
nsimpson=N.zeros(nptos)

for i in range(nfun):
    fn=S.lambdify(x,funciones[i],'numpy')
    exacta[i]=float(S.integrate(funciones[i],(x,*intervalos[i]))) #integración exacta con sympy
    
    for j in range(nptos):
        pp=N.array(intervalos[i]).astype(float)
        xx=N.linspace(*pp,puntos[j]) #con cada iteración en j creamos nuevos subintervalos
        #cada vez de una cifra más
        yy=fn(xx) 
        nsimpson[j]=sc.simps(yy,xx) #hacemos simpson
        ntrap[j]=sc.trapz(yy,xx) #hacemos trapecio
        
    plt.figure(i)
    plt.title(S.latex(funciones[i])) #modtramos la función en cada caso
    plt.plot(puntos,exacta[i]*N.ones(nptos),label='Exacta')
    plt.plot(puntos,ntrap,label='Trapecio')
    plt.plot(puntos,nsimpson,label='Simpson')
    plt.grid()
    plt.legend()
plt.show()