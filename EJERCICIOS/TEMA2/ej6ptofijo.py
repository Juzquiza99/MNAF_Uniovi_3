# -*- coding: utf-8 -*-
"""
Created on Mon Sep 23 12:50:19 2019

@author: UO264982
"""

#Ejerc 6 Pto fijo

import sympy as S
import numpy as N
import matplotlib.pyplot as plt
import scipy.optimize as so
x=S.symbols('x',real=True)

#Utilizamos vectores
def ptofijo(g,x0,maxiter,tolx):
    x = N.zeros(maxiter+1) #Creamos el vector con de tamano del numero de iteraciones
    x[0]=x0 #Valor inicial x0
    for i in range(maxiter):
        x[i+1]=g(x[i])
        if abs(x[i+1]-x[i])<tolx:
            return [x[i+1],x[0:i+2]]

g=(x**2*S.exp(x)+4)/(S.exp(x)*(x+1))
gn=S.lambdify(x,g,'numpy')
g2=S.log(4/x)
gn2=S.lambdify(x,g2,'numpy')

resul=ptofijo(gn,1,1000,10**(-6))
print (resul) #pto fijo

t=N.linspace(0,20,5)

plt.figure()
plt.plot(t,resul[1])
plt.grid()
plt.show()


#Ejerc 7 Pto fijo

def odenco(xn,alfa):#funcion para obtener el orden de converg de la sucesion
    pn=N.zeros(len(xn))
    for i in range(xn.shape[0]):
        pn[i]=N.log(abs((alfa-xn[i+2])/(alfa-xn[i+1])))/N.log(abs(((alfa-xn[i+1])/(alfa-xn[i]))))
        return pn[i]
    
print('Promedio de g1(x)')
print(odenco(resul[1],resul[0]))

resul2=ptofijo(gn2,1,1000,10**(-6))
print(resul2) #ptofijo
print('Promedio de g2(x)')
print(odenco(resul2[1],resul2[0]))


#NEWTON

def newton(f,fp,xa,n=100, tolx=1e-12,toly=1e-16):
    '''método de Newton para una función f y su derivada fp'''
    sol=[] #creamos lista
    for i in range (n):
        x=xa-f(xa)/fp(xa)
        if abs(x-xa)<tolx or abs(f(x)-f(xa))<toly:
            break
        sol.append(x)
        xa=x
               
    return (xa,i) #"solución y número de iteraciones hasta obtenerlo

def f(x):
    return x*N.e**(x)-4 #función f

def fp(x):
    return N.e**(x)*(1+x) #derivada función f

print(newton(f,fp,1))

#STEFFENSEN

def steffensen(f,xa,n=100, tolx=1e-12,toly=1e-16):
    '''método de Steffensen para una función f'''
    sol=[] #creamos lista
    for i in range (n):
        x=xa-(f(xa))**2/(f(xa+f(xa))-f(xa))
        if abs(x-xa)<tolx or abs(f(x)-f(xa))<toly:
            break
        sol.append(x)
        xa=x
               
    return (xa,i)

print(steffensen(f,1))

#SECANTE
def secante(f,xb,xa,n=100, tolx=1e-12,toly=1e-16):
    '''método de Newton modificado sin derivada fp'''
    sol=[] #creamos lista
    for i in range (n):
        x=xa-f(xa)*((xa-xb)/(f(xa)-f(xb)))
        if abs(x-xa)<tolx or abs(f(x)-f(xa))<toly:
            break
        sol.append(x)
        xb=xa
        xa=x
        
               
    return (xa,i)

print(secante(f,0,1))

#MODULOS DE PYTHON PUNTO FIJO
#MÉTODO DE NEWTON
solu1=so.newton(f,0)
print(solu1)

#MÉTODO DE PUNTO FIJO
solu2=so.fixed_point(gn,[1,2]) 
'''Función donde encontremos intervalo de confianza y dicho intervalo de confianza
'''
print(solu2)
