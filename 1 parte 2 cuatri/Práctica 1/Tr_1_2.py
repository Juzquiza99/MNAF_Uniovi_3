# -*- coding: utf-8 -*-

#Autor: Javier Uzquiza López

import numpy as np
import matplotlib.pyplot as plt
import scipy.spatial as spatial
'''
Indicaciones de uso del programa:
    modificación de los distintos parámetros que aparecen en la práctica
    según se desee. Para obtener la energía total correctamente modificar los
    coeficientes correspondientes a cada tipo de partícula según la proporción
    en la que se encuentren
'''


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
N=100 #número total de partículas
nmedio=int(N/2)
l=15 #longitud de la caja
npasos=500

dt=0.01
pausa=0.01
pasos=10

epsilon = 0.25 #distancia de choque de las partículas
kb = 0.01 #constante de Boltzmann
m=np.zeros(N)
m1=1 #masa de las partículas de tipo 1
m2=40 #masa de las partículas de tipo 2
m[0:nmedio]=m1
m[nmedio:]=m2
T = np.zeros(N)
T1=100 #temperatura inicial de las partículas de tipo 1
T[0:nmedio]=T1
energia0 = np.random.exponential(kb*T,(1,N)) #distribución exponencial de la energía

v0 = (2*energia0/m)**0.5 #cálculo de la velocidad inicial


#Simulación
fig=plt.figure(figsize=(6,6))
ax=fig.add_subplot(111) #Eje x
ax.set_xlim((0,l)) #Límites ejes
ax.set_ylim((0,l))
x=(l*np.random.rand(N,2))

point1,=ax.plot(x[:nmedio,0],x[:nmedio,1],'ro') 
point2,=ax.plot(x[nmedio:,0],x[nmedio:,1],'bo')
angu0=2*np.pi*(np.random.rand(N))
v=v0.T*np.array([np.cos(angu0), np.sin(angu0)]).T

#número de representaciones a realizar
nrepre=40
 

#Función que modela el choque entre partículas
def choque(x1,x2,v1,v2,m1,m2):    
    dist = (((x1-x2)[0])**2 + ((x1-x2)[1])**2)**0.5
    norm = (x2-x1)/dist
    tang = np.array([-norm[1],norm[0]])
    if np.dot(v1,norm)-np.dot(v2,norm)>=0:
        v1norm = np.dot(norm,v1)
        v2norm = np.dot(v2,norm)
        v1norm,v2norm = (2*v2norm*m2+v1norm*(m1-m2))/(m1+m2),(2*v1norm*m1+v2norm*(m2-m1))/(m1+m2)
        v1tang = np.dot(v1,tang)
        v2tang = np.dot(v2,tang)
        v1 = norm*v1norm + tang*v1tang
        v2 = norm*v2norm + tang*v2tang
    return v1,v2

energias = np.zeros(N)
enermedia1=np.zeros(nrepre)
enermedia2=np.zeros(nrepre)
ener1=np.zeros(nrepre)
ener2=np.zeros(nrepre)
enertotal=np.zeros(nrepre)

#Modelización del choque contra las paredes de la caja
for k in range(nrepre):
    for i in range(npasos):
        x=x+dt*v
        for j in range(N):
            if x[j,0] <=0 :
                if v[j,0]<0:
                    v[j,0]=-v[j,0]
            if  x[j,0]>=l:
                if v[j,0]>0:
                    v[j,0]=-v[j,0]
                    
            if x[j,1] <=0 :
                if v[j,1]<0:
                    v[j,1]=-v[j,1]
                    
            if x[j,1]>=l:
                if v[j,1]>0:
                    v[j,1]=-v[j,1]
                
        
            energias[j]=0.5*m[j]*(v[j,0]**2+v[j,1]**2)
        

        points_tree = spatial.cKDTree(x)
        pairs = points_tree.query_pairs(epsilon)

        for ipair in pairs:
            v[ipair[0],:],v[ipair[1],:]=choque(x[ipair[0],:],x[ipair[1],:],v[ipair[0],:],v[ipair[1],:],m[ipair[0]],m[ipair[1]])

        if i % pasos ==0:
            point1.set_data(x[:nmedio,0],x[:nmedio,1])
            point2.set_data(x[nmedio:,0],x[nmedio:,1]) 
            plt.pause(pausa)
            
#Cálculo de las energías de cada tipo de partícula            
    enermedia1=np.mean(energias[:nmedio])
    ener1[k]=enermedia1
    enermedia2=np.mean(energias[nmedio:])
    ener2[k]=enermedia2
    enermediatotal=enermedia1+enermedia2
    enertotal[k]=0.5*ener1[k]+0.5*ener2[k]

 
xt=np.linspace(npasos,nrepre*npasos,nrepre)
X=np.concatenate(([0],xt),axis=None)
ener2f=np.concatenate(([0],ener2),axis=None)
ener1f=np.concatenate(([kb*T1],ener1),axis=None)
enertotalf=np.concatenate(([enertotal[0]],enertotal),axis=None)

#Cálculo de las temperaturas a partir de las energías
temp1=ener1f/kb
temp2=ener2f/kb
temptotal=enertotalf/kb

#Representación de la variación de la temperatura en función del número de pasos
plt.figure()
plt.title('100 partículas (50 de cada tipo)')
plt.grid()
plt.ylabel('Temperatura')
plt.xlabel('Número de pasos')
plt.plot(X,temp1,'r',label='Partículas tipo 1')
plt.plot(X,temp2,'b',label='Partículas tipo 2')
plt.plot(X,temptotal,label='Partículas totales')
plt.legend()
plt.show()
