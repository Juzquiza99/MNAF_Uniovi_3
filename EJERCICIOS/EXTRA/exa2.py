# -*- coding: utf-8 -*-
"""
Created on Sun Dec  1 18:43:37 2019

@author: javie
"""
import numpy as N
import matplotlib.pyplot as plt
import scipy.interpolate as si
import scipy.optimize as SO
import sympy as S

#EXAMEN OTRA CLASE

#1- Hermite (ya hecho aparte)

#2

x=[2.5,3.5,5,6,7.5,10,12.5,15,17.5,20]
y=[7,5.5,3.9,3.6,2.1,2.8,2.6,2.4,2.3,2.3]

d1 = N.diff(y)/N.diff(x)
print(d1)

d2=N.diff(d1)/N.diff(x[:len(x)-1])
print(d2)

'''Extra'''
c=si.interp1d(x,y, kind='quadratic')
X=N.linspace(2.5,20,201)
z=c(X)
dz1=N.diff(z)/N.diff(X)
dz2=N.diff(dz1)/N.diff(X[1:])

plt.figure()
plt.plot(x,y,'ro')
plt.plot(X,z)
plt.plot(X[1:],dz1)
plt.plot(X[2:],dz2)
plt.grid()
plt.show()



X=N.linspace(0,2*N.pi,201)
t=N.sin(X)
dt=N.diff(t)/N.diff(X) #Primera derivada
dt2=N.diff(dt)/N.diff(X[:len(t)-1]) #Segunda derivada
plt.figure()
plt.plot(X,t)
plt.plot(X[:200],dt)
plt.plot(X[:199],dt2)
plt.grid()
plt.show()

'''---------------------------------------------------------'''

#Ej3

x=[2.5,3.5,5,6,7.5,10,12.5,15,17.5,20]
x=N.array(x)
y=[7,5.5,3.9,3.6,2.1,2.8,2.6,2.4,2.3,2.3]
y=N.array(y)
#Ajuste mediante polinomio de segundo grado:
funcrec=lambda x,a,b: x/(a*x+b)
funarc=lambda x,a,b,c,d: a*N.arctan(b*x-c)+d
coef1=N.polyfit(x,y,2) #pol.grado 2
coef2=N.polyfit(1/x,1/y,1) #crecimiento
coef3,cov3=SO.curve_fit(funarc,x,y)#arctang
coef4,cov4=SO.curve_fit(funcrec,x,y)#crecimiento

X = N.linspace(x[0],x[-1],201)

plt.figure()
plt.plot(x,y,'ro')
plt.plot(X,z,label='Ajuste quadratic Spline') #Función interpolada con Cubic Spline
plt.plot(X,N.polyval(coef1,X),label='poly2')
plt.plot(X,1./(N.polyval(coef2,1./X)),label='Crecimiento lineal')
plt.plot(X,funcrec(X,*coef4),label='Crecimiento no lineal')
plt.plot(X,funarc(X,*coef3),label='Arcontangente')
plt.legend()
plt.grid()
plt.show()

#--------------------------------------
#Ej:2.1

def deriv(h,x0,a,f):
    der1=(1./6*h)*(-11*f(a)+18*f(a+h)-9*f(a+2*h)+2*f(a+3*h))
    der2=(1./6*h)*(-2*f(x0)-3*f(a)+6*f(a+h)-f(a+2*h))
    return [der1,der2]
f1=lambda x:N.sin(N.exp(x**2))
print(deriv(1,0,1,f1)[1]) #con x0=0
print(deriv(0.5,0.5,1,f1)[1]) #con x0=0.5
print(deriv(0.5,1,1,f1)[0]) #con x0=0.5

#Ej:3
x=S.symbols('x',real=True)
f3=S.sin(x)/((x)**(1./4)) #función a integrar
sol=float(S.integrate(f3, (x,0,1))) #Usando Sympy
print(sol)

X=N.linspace(0,1,201)
fn1=S.lambdify(x,f3,'numpy')
Y=fn1(X)
sol2=integracion(fn1,[0,1],1,201) #Función integración hecha en int3-py
#En este caso hemos utilizado el trapecio abierto para resolverlo, aunque en
#definitiva, cualquier fórmula abierta(no incluye los puntos límite de los intervalos),
#nos hubiera funcionado
print(sol2)
