# -*- coding: utf-8 -*-
"""
Editor de Spyder

Este es un archivo temporal
"""

import numpy as np
import matplotlib.pyplot as plt
import scipy.spatial as spatial
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
N=100 #número partículas
#Aproximación exponencial
#E=kb*T
energia0=np.random.exponential(0.5,N) #A partir de la distribución exponencial
#de energías calculamos la velocidad inicial de las partículas
m=1 #masa disco
l=10 #lado caja
npasos=10000
dt=0.01
v=np.sqrt(2*energia0/m) #módulo de la velocidad
pausa=0.01
pasosrepre=100
kb=0.01
#r=(rx,ry)+v*dt

fig=plt.figure(figsize=(6,6))
ax=fig.add_subplot(111) #Eje x
ax.set_xlim((0,l)) #Límites ejes
ax.set_ylim((0,l))

x=l*np.random.rand(2,N)
point,=ax.plot(x[0],x[1],'yo') 

angu0=2*np.pi*(np.random.rand(N))
v=np.array([v*np.cos(angu0), v*np.sin(angu0)])


#Función choque
def choque(r12,v1,v2): #variables que introducimos son vectores
    distrad=np.linalg.norm(r12)
    uc=r12/distrad
    up=np.array([-r12[1],r12[0]])/distrad
    vc1=np.dot(v1,uc)
    vp1=np.dot(v1,up)
    vc2=np.dot(v2,uc)
    vp2=np.dot(v2,up)
    #Para evitar que las partículas se nos junten y se queden unidas
    if (vc1-vc2)<0:
        v1,v2=v1,v2
    
    else:
        vc1,vc2=vc2,vc1
        v1=vc1*uc+vp1*up
        v2=vc2*uc+vp2*up
    
    return v1,v2

epsilon=0.25 #distancia de choque

#KDTREE
presiontodas=np.zeros(npasos)
presion=np.zeros(int(npasos/pasosrepre))
for i in range(npasos):
    x=x+v*dt
    for j in range(N):
        if x[0,j] <=0:
            if v[0,j]<0:
                v[0,j]=-v[0,j]
                presiontodas[i]+=0.5*m*np.abs(v[0,j])/l/dt
        if x[0,j]>=l:
            if v[0,j]>0:
                v[0,j]=-v[0,j]
                presiontodas[i]+=0.5*m*np.abs(v[0,j])/l/dt
        if x[1,j] <=0:
            if v[1,j]<0:
                v[1,j]=-v[1,j]
                presiontodas[i]+=0.5*m*np.abs(v[1,j])/l/dt
        if x[1,j]>=l:
            if v[1,j]>0:
                v[1,j]=-v[1,j]
                presiontodas[i]+=0.5*m*np.abs(v[1,j])/l/dt
            
        if i % int(npasos/pasosrepre)==0:
            presion[int(i/pasosrepre)]=np.mean(presiontodas[i-pasosrepre:i])
        
    points_tree=spatial.cKDTree(x.T)
    pairs=points_tree.query_pairs(epsilon)
        
    for ipair in pairs:
        v[:,ipair[0]],v[:,ipair[1]]=choque(x[:,ipair[1]]-x[:,ipair[0]],v[:,ipair[0]],v[:,ipair[1]])
    
    if i % pasosrepre ==0:
        point.set_data(x[0],x[1]) 
            
        plt.pause(pausa)
      

#HISTOGRAMA DE LAS ENERGÍAS DE LAS PARTÍCULAS
energia=np.zeros(N)
for i in range(N):
    energia[i]=0.5*m*(v[0,i]**2+v[1,i]**2)  

fig2,ax2=plt.subplots()
ax2.hist(energia,bins=25,range=(0,2*np.mean(energia)))
plt.show()

#Energía al final (veamos si se ha conservado)
enerfin=np.mean(energia)
print('Energía inicial: E=Kb*T=50*0.01=0.50')
print('Energía al final:')
print(enerfin)


#PRESIÓN (analizamos los choques contra las paredes)
#dtarray=np.linspace(0,dt*npasos,npasos)
dtarray2=np.linspace(0,dt*npasos,int(npasos/pasosrepre))
plt.figure()
#plt.plot(dtarray,presiontodas)
plt.plot(dtarray2,presion)
plt.show()


#coefs gas ideal y de van der waals
presionmedia=np.sum(presion[1:-1])/int(npasos/pasosrepre)
area=l*l
adiscos=np.pi*epsilon**2
areareal=area-adiscos
tf=enerfin/kb
gasideal=(presionmedia*area)/(N*kb*tf)
gasvdw=(presionmedia*areareal)/(N*kb*tf)

print('Coeficiente gas ideal:')
print(gasideal)
print('Coeficiente gas Van der Waals:')
print(gasvdw)



