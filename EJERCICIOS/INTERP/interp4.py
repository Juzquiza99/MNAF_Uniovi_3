# -*- coding: utf-8 -*-
"""
Created on Fri Oct 25 17:03:10 2019

@author: UO264982
"""


#DIFERENCIAS DIVIDIDAS DE NEWTON
import numpy as np
import matplotlib.pyplot as plt
import scipy.interpolate as si 

#Cálculo de los coeficientes

def difdivnewton(x,y):
    n=x.shape[0]
    tabla=np.zeros((n,n))
    tabla[:,0]=y
    for col in range(1,n):
        for fil in range(n):
            tabla[fil,col]=(tabla[fil-1,col-1]-tabla[fil,col-1])/(x[fil-col]-x[fil])
    c=np.diag(tabla) #Obtenemos los coeficientes en el orden inverso al esperado, para
#invertir dicho orden: c=c[::-1], aunque no es necesario
    return tabla, c #Que nos devuelva la tabla y los coeficientes

#Función evaluación de la forma de Newton
def evalu(x,z,c): #z es el punto donde evaluamos
    R=c[-1] #Ultimo coeficiente
    for i in range(len(c)-1,-1,-1):
        R=R*(z-x[i])+c[-i]
    return R


#EJERCICIO 6
'''Dado un soporte de 7 puntos esquiespaciados en el intervalo [−5,5], y los
valores de la función f (x) = x4 −2x + 1 en los mismos, calcular la tabla de
diferencias divididas.'''
x = np.linspace(-5,5,7)
f=lambda x:x**4-2*x+1
y=f(x)
print(difdivnewton(x,y))
t=difdivnewton(x,y)[1] #coeficientes de la tabla
print(evalu(x,1,t))


#EJERCICIO 7

f=lambda x: 1./(1+x**2)

N = [5,9,13,17]
X = np.linspace(-5,5,201)
for n in N:
    x=np.linspace(-5,5,n)
    sol=si.lagrange(x,f(x)) #Calculo de los coeficientes por Lagrange
    fig=plt.figure(1)
    plt.plot(x,f(x),'ro',label='datos')
    plt.plot(X,f(X),label='función')
    plt.plot(X,sol(X),label='polinomio')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.grid()
    plt.show()
    error=np.abs(np.max(f(X)-sol(X)))
    print('Error:')
    print(error)

#Para aminorar  el error: utilizar las raíces de los polinom. de Chebysev, es decir,
    #cambiamos los x
#x=5*np.cos((2*np.arange(n)+1)*np.pi/(2*n))

#EJERCICIO 8
for n in N:
    #xk=((a+b)/2)+((b-a)/2)*cos((2k-1)pi/2*n), siendo a y b el primero y el último de los puntos que tomamos
    x=5*np.cos((2*np.arange(n)+1)*np.pi/(2*n))
    sol=si.lagrange(x,f(x))
    fig=plt.figure(1)
    plt.plot(x,f(x),'ro',label='datos')
    plt.plot(X,f(X),label='función')
    plt.plot(X,sol(X),label='polinomio')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.grid()
    plt.show()
    error=np.abs(np.max(f(X)-sol(X)))
    print('Error:')
    print(error)
     
#Escogiendo nosotros los mejores puntos(Chebysev), cuantos más sean, mejor será
    #la aproximación
    

#Pero si los puntos ya me vienen dados, ¿Cómo puedo aminorar el error de la 
    #aproximación?: cubic spline
#EJERCICIO 9
for n in N:
    x=np.linspace(-5,5,n)
    y=f(x)
    sol=si.interp1d(x,y, kind='cubic')
    fig=plt.figure(1)
    plt.plot(x,f(x),'ro',label='datos')
    plt.plot(X,f(X),label='función')
    plt.plot(X,sol(X),label='polinomio')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.grid()
    plt.show()
    error=np.abs(np.max(f(X)-sol(X)))
    print('Error:')
    print(error)
    

#EJERCICIO 10 MÁSTIL BARCO
x=[126,365,506,527,562,703]
y=[0.5,1.3,2,4.5,6,8.5]
poly1=si.lagrange(x,y)
poly2=si.interp1d(x,y, kind='cubic')
poly3=si.interp1d(x,y, kind='slinear')
X=np.linspace(x[0],x[-1],201)
Z1=poly1(X)
Z2=poly2(X)
Z3=poly3(X)

plt.figure()
plt.plot(x,y,'ro')
plt.plot(X,Z1,'y',label='Lagrange Interpolate')
plt.plot(X,Z2,'b',label='Cubic Spline')
plt.plot(X,Z3,'r',label='Linear Spline')
plt.grid()
plt.legend()
plt.show()


#DD Gener.
#EJERCICIO 3
x=np.array([0,0,125,125,240,240])
y=np.array([0,0,6500,65,13000,70])
pkro1=si.KroghInterpolator(x[0::2],y[0::2])
pkro2=si.KroghInterpolator(x[0::2],y[1::2])

X=np.linspace(0,240,1001)

fig=plt.figure(1)
plt.plot(x[0::2],y[0::2],'ro',label='datos')
plt.plot(X,pkro1(X))
plt.grid()
plt.show()

fig=plt.figure(2)
plt.plot(x[1::2],y[1::2],'ro',label='datos')
plt.plot(X,pkro2(X))
plt.grid()
plt.show()
