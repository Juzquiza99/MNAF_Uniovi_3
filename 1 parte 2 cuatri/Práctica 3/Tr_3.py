#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar  5 17:13:51 2020

@author: uo264982
"""
#Autor: Javier Uzquiza López
'''
Tras haber comentado con algunos compañeros los resultados obtenidos, el valor
de la energía total que se obtiene al utilizar la base de fourier (sin importar el número de funciones utilizadas)
es superior al esperado (entorno a -17.5). Habiendo buscado el posible fallo y reescrito
gran parte del código para intentar solucionarlo, no lo he logrado. Para Slater y
Gauss el resultado obtenido en cada caso sí que parece favorable.
'''

import numpy as np
import matplotlib.pyplot as plt
import scipy.linalg as sc

np.set_printoptions(precision=4,suppress=True) #precisión de 4 cifras decimales
#Cálculo y pintado del potencial
xmin=0
xmax=10
ptosmallado=1001
nx=np.linspace(0,10,ptosmallado) #mallado
N=5 #número de átomos
Z=1 #número atómico
posiato=np.linspace(xmin,xmax,N+2) #posiciones que ocupan los átomos
delta=0.1
nfun=5 #número de funciones de base
beta=1 
xato=posiato[1:-1]
numelectrones=5

#Seleccionamos si queremos Slater o Gauss o Fourier
slater=1
gauss=0
ondas=0

#array donde se almacenará información sobre el potencial provocado por cada átomo
vato=np.zeros((ptosmallado,N)) 
for i in range(N):
    vato[:,i]=-Z/(np.sqrt((nx[:]-xato[i])**2+delta))
    
vtotal=np.sum(vato,axis=1) #potencial toatal

#Representación consecuencia de cada átomo
plt.figure()
plt.title('Potencial para 5 átomos (Z=1)')
plt.xlabel('x (a0)') #Unidades de longitud: radio de Böhr
plt.ylabel('V (Eh = 27.2 eV)') #Unidad de energía: Hartrees; 1Eh=2Ry=27.2eV
plt.grid()
plt.plot(nx,vtotal)
plt.show()

#------------------------------------------------------------------------------
#------------------------------------------------------------------------------


#Funciones de onda a partir de las distintas bases
funbases=np.zeros((ptosmallado,nfun),complex)

for j in range(nfun):
    if slater==1:
        funbases[:,j]=np.exp(-beta*abs(nx[:]-xato[j]))
        norma=np.trapz((funbases[:,j])**2,nx)
        funbases[:,j]=(funbases[:,j])/np.sqrt(norma)
        norma=np.trapz((funbases[:,j])**2,nx) #Comprobamos que están normalizadas
    
    if gauss==1:
        funbases[:,j]=np.exp(-beta*(nx[:]-xato[j])**2)
        norma=np.trapz((funbases[:,j])**2,nx)
        funbases[:,j]=(funbases[:,j])/np.sqrt(norma)
    
    if ondas==1:#ondas planas fourier
        k=np.zeros(nfun)
        L=xmax-xmin
        n=np.linspace(int(-nfun/2),int(nfun/2),nfun)
        k[:]=(2*np.pi*n[:]/L)
        funbases[:,j]=np.exp(1j * k[j] *nx[:])
        norma=np.trapz(np.conj(funbases[:,j])*(funbases[:,j]),nx)
        funbases[:,j]=(funbases[:,j])/np.sqrt(norma)
        

#Representación de las bases de funciones.
plt.figure()
if slater==1:
    plt.title('Base de funciones (Slater)')
if gauss==1:
    plt.title('Base de funciones (Gauss)')
if ondas==1:
    plt.title('Base de funciones (Fourier)')
plt.xlabel('x (a0)')
plt.ylabel(r'$\psi$ (x)')
plt.grid()
plt.plot(nx,funbases)


#------------------------------------------------------------------------------
#------------------------------------------------------------------------------

#H=T+V=-0.5*(d2/dx2)+V(x)
#Cálculo de la derivada segunda, previa al hamiltoniano
derivseg=np.zeros((ptosmallado,nfun))  
for j in range(nfun):
    derivseg[1:-1,j]=(funbases[2:,j]+funbases[:-2,j]-2*funbases[1:-1,j])/((xmax-xmin)/ptosmallado)**2
plt.figure()
plt.grid()
plt.title('Derivada segunda')
plt.xlabel('x')
plt.ylabel('phi''(x)')
plt.plot(nx[1:-1],derivseg[1:-1,:])
plt.show()

#Cálculo de la matriz de solape S
S=np.zeros((nfun,nfun))
H=np.zeros((nfun,nfun))


for i in range(nfun):
    for j in range(nfun):
        S[i,j]=np.trapz((funbases[:,j])*np.conj(funbases[:,i]),nx)
        H[i,j] = np.trapz(np.conj(funbases[:,i]*(-0.5)*derivseg[:,j]),nx) + np.trapz(funbases[:,i]*vtotal[:]*np.conj(funbases[:,j]),nx)
print('Matriz S:')
print(S)
print('Matriz H:')
print(H)

#Autovalores y autovectores
energias,vectores=sc.eig(H,S)
print('Energías:')
print(energias)
print('Autovectores:')
print(vectores)

#Se ordenan las autovalores de energía
iorden=np.argsort(energias)
energias=energias[iorden]
print('Energías ordenadas:')
print(energias)
print('Autovectores ordenados:')
vectores=vectores[:,iorden]
print(vectores)

#Representación de los funciones de onda solución de H
funcibasesH=np.dot(funbases,vectores)
print('Funciones de onda:')
print(funcibasesH)
plt.figure()
plt.title('Autofuciones de onda solución de H (Fourier)')
plt.grid()
plt.xlabel('x (a0)')
plt.ylabel(r'$\psi$ (x)')
plt.plot(nx,funcibasesH)
plt.show()


#Añadimos los electrones y calculamos el valor total de la energía
energiatot=0
cociente=numelectrones//2

for i in range(cociente):
    energiatot += 2*energias[i]
if np.mod(numelectrones,2) != 0:
    energiatot += energias[cociente]

print(energiatot)

