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
npasos=1000
dt=0.01
v=1 #módulo de la velocidad
pausa=0.01
pasos=10
N=100 #número partículas
#r=(rx,ry)+v*dt

fig=plt.figure(figsize=(6,6))
ax=fig.add_subplot(111) #Eje x
ax.set_xlim((0,l)) #Límites ejes
ax.set_ylim((0,l))

x=l*np.random.rand(2,N)
point,=ax.plot(x[0],x[1],'ro') 

angu0=2*np.pi*(np.random.rand(N))
v=np.array([v*np.cos(angu0), v*np.sin(angu0)])

for i in range(npasos):
    x=x+v*dt
    for j in range(N):
        if x[0,j] <=0:
            v[0,j]=-v[0,j]
        if x[0,j]>=l:
            v[0,j]=-v[0,j]
        if x[1,j] <=0:
            v[1,j]=-v[1,j]
        if x[1,j]>=l:
            v[1,j]=-v[1,j]
            
    if i % pasos ==0:
            point.set_data(x[0],x[1]) 
            
            plt.pause(pausa)


#HISTOGRAMA DE LAS ENERGÍAS DE LAS PARTÍCULAS
energia=np.zeros(N)
for i in range(N):
    energia[i]=0.5*m*(v[0,i]**2+v[1,i]**2)
    
fig2,ax2=plt.subplots()
ax2.hist(energia,bins=25,range=(0,2*np.mean(energia)))
plt.show()

#Función choque
def choque(r12,v1,v2): #variables que introducimos son vectores
    distrad=np.linalg.norm(r12)
    uc=r12/distrad
    up=uc
    up[0]=-uc[1]
    up[1]=uc[0]
    vc1=np.dot(v1,uc)
    vp1=np.dot(v1,up)
    vc2=np.dot(v2,uc)
    vp2=np.dot(v2,up)
    vc1,vc2=vc2,vc1
    v1=vc1*uc+vp1*up
    v2=vc2*uc+vp2*up
    
    return v1,v2
    
   
    