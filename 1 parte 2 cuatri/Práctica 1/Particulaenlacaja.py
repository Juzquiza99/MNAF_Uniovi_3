# -*- coding: utf-8 -*-
"""
Editor de Spyder

Este es un archivo temporal
"""

import numpy as np
import matplotlib.pyplot as plt
'''
Datos del problema:
lado caja: 10
masa disco 1
ci:
posicion inicial (x0) aleatoria
vo=1, direccion aleatoria
dt=0.01
num pasos:10000
pasos entre reps:10
pausa entre repres:0.01s
'''
m=1 #masa disco
l=10 #lado caja
npasos=10000
dt=0.01
v=1 #módulo de la velocidad
pausa=0.01
pasos=10
#r=(rx,ry)+v*dt

fig=plt.figure(figsize=(6,6))
ax=fig.add_subplot(111) #Eje x
ax.set_xlim((0,l)) #Límites ejes
ax.set_ylim((0,l))

x=l*np.random.rand(2)
point,=ax.plot(x[0],x[1],'ro') 


angu0=2*np.pi*(np.random.rand())
v=v*np.array([np.cos(angu0), np.sin(angu0)])

for i in range(npasos):
    x=x+dt*v
    if x[0] <=0 or x[0]>=l:
        v[0]=-v[0]
    if x[1] <=0 or x[1]>=l:
        v[1]=-v[1]
        
    if i % pasos ==0:
        point.set_data(x[0],x[1]) 
        
        plt.pause(pausa)

