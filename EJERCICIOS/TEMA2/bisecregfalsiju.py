# -*- coding: utf-8 -*-
"""
Created on Mon Sep 16 13:23:11 2019

@author: uo243498
"""

#METODOS DE INTERVALO

import numpy as N
import matplotlib.pyplot as plt
import scipy.optimize as S


#Programar la funcion lambda f(x)=x e^x - 4 y representarla en [0,2]
f = lambda x: x*N.exp(x)-4 #usamos el de numpy porque estamos con la funcion lambda
a,b=(0,2) #intervalo en el que quiero hallar el cero de la funcion
maxiter, tolX, tolF = (1000,1E-6,1E-9)

#Pinto la grafica para hacerme una idea de por donde van los tiros
X= N.linspace(a,b)
plt.plot(X, f(X))
plt.grid()

#Veo que es continua y que en ella se cumple el teorema de Bolzano.



#Programar el modulo bisec con argumentos {f, [a,b], maxiter, tolx, tolf} y usarla para encontrar la raiz de f(x) en 0,2

def bisec (f, a,b, maxiter, tolx, tolf):
    fa=f(a) #establezco esto al principio para no hacer operaciones de mas 
    fb=f(b)
    if fa*fb > 0:
        raise ValueError('No se cumple el teorema de Bolzano') #da un mensaje de error
    elif N.abs(fa)<tolf:
        return ('Hay un cero en a')
    elif N.abs(f(b))<tolf:
        return ('Hay un cero en b')
    
    n = N.ceil(N.log2(N.abs(b-a)/tolX)).astype(int) #redonear es la formula N.ceil, que redondea hacia el numero entero siguiente si no le digo nada (sale el resultado en tipo float)
    #necesito para el bucle un numero tipo entero .astype (int)
   
    minimo = min(n,maxiter)
    lista = []  #voy a ir almacenando aqui los puntos medios que me salen
    #Ahora en vez de almacenar los valores en una lista los almaceno en un vector
    iter=N.zeros(maxiter) #creo un vector con maxiter ceros
    
    for i in range(minimo):
        c = 0.5*(a+b)   #c es el punto medio del intervalo  
        fc=f(c)
        lista.append(c)
        iter[i]=c
        
        if N.abs(fc)<tolf:
            return [c, lista, iter[:i+1]]        #el resto de valores de iter son ceros
        elif fa*fc<0: #cojo la mitad izquierda
            b=c #entonces mi nuevo intervalo es (a,c)
            fb=fc
        elif fb*fc<0:
            a=c
            fa=fc
        if N.abs(a-b)<tolx: 
            return [c, lista, iter[:i+1]]
  
resultado= bisec(f,a,b,maxiter,tolX,tolF)
print ('El resultado con metodo de intervalo es:')
print (resultado)


#Metodo regula falsi
def regulafalsi (f, a,b, maxiter, tolx, tolf):
    fa=f(a) #establezco esto al principio para no hacer operaciones de mas 
    fb=f(b)
    if fa*fb > 0:
        raise ValueError('No se cumple el teorema de Bolzano') #da un mensaje de error
    elif N.abs(fa)<tolf:
        return ('Hay un cero en a')
    elif N.abs(f(b))<tolf:
        return ('Hay un cero en b')

   
    lista = []  #voy a ir almacenando aqui los puntos medios que me salen
    #Ahora en vez de almacenar los valores en una lista los almaceno en un vector
    iter=N.zeros(maxiter) #creo un vector con maxiter ceros
    
    for i in range(maxiter):
        c = a-fa*(b-a)/(fb-fa)   #c es el punto medio del intervalo  
        fc=f(c)
        lista.append(c)
        iter[i]=c
        
        if N.abs(fc)<tolf:
            return [c, lista, iter[:i+1]]        #el resto de valores de iter son ceros
        elif fa*fc<0: #cojo la mitad izquierda
            b=c #entonces mi nuevo intervalo es (a,c)
            fb=fc
        elif fb*fc<0:
            a=c
            fa=fc
        if N.abs(a-b)<tolx: 
            return [c, lista, iter[:i+1]]
  
resultadoregula = regulafalsi(f,a,b,maxiter,tolX,tolF)
print ('Regula falsi')
print (resultadoregula)
   
x2,s2= S.bisect(f,a,b,xtol=tolX,rtol=tolF, maxiter=maxiter,full_output=True )
print ('Bisect:')
print(x2,s2)

x3,s3=S.brentq(f,a,b,xtol=tolX,rtol=tolF, maxiter=maxiter,full_output=True)
print ('Brentq')
print (x3,s3)

x4,s4=S.brenth(f,a,b,xtol=tolX,rtol=tolF, maxiter=maxiter,full_output=True)
print ('Brenth')
print (x4,s4)

x5,s5=S.ridder(f,a,b,xtol=tolX,rtol=tolF, maxiter=maxiter,full_output=True)
print ('Ridder')
print (x5,s5)