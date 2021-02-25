# -*- coding: utf-8 -*-

#Autor: Javier Uzquiza López

import numpy as np
import matplotlib.pyplot as plt
import scipy.spatial as spatial
import scipy.optimize as so

'''
Indicaciones de uso del programa:
    dejar de comentar la parte de la presión vs área y su representación cuando
    se desee (última parte del programa). En este momento se representa directamente
    la parte de la presión vs área^-1 (comentar dichas partes cuando no se desee).

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

m=1 #masa del disco
N=150 #número partículas
epsilon=0.25 #distancia de choque

'''Utilizar un tipo de representación u otro según la gráfica que se quiera obtener''
'''
#Representación en función del inverso del área
areadisco=N*np.pi*epsilon**2
areainv=np.linspace (1/(100-areadisco),1/(1500-areadisco),15) #Tener en cuenta el área de los discos para el cálculo de la presión
area=areainv**(-1)
l=np.sqrt(area)
areainv2=np.linspace(1/100,1/1500,15) #Para la representación

#Representación en función del área
'''
area1=np.linspace(100,1500,15)
area1part=np.linspace(100-areadisco,1500-areadisco,15)
l=np.sqrt(area1)
'''
#Aproximación exponencial
#E=kb*T

npasos=5000
dt=0.01
pausa=0.01
pasosrepre=100
kb=0.01
T=25

#A partir de la distribución exponencial
#de energías calculamos la velocidad inicial de las partículas
energia0=np.random.exponential(kb*T,N)
v0=np.sqrt(2*energia0/m) #módulo de la velocidad



#Función que determina el choque entre las partículas
def choque(r12,v1,v2):
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


presiontodas=np.zeros(npasos)
presion=np.zeros(int(npasos/pasosrepre))
presion2=np.zeros(len(l))

for k in range(len(l)):
    fig=plt.figure(figsize=(6,6))
    ax=fig.add_subplot(111)
    ax.set_xlim((0,l[k])) #Límites ejes
    ax.set_ylim((0,l[k]))
    
    x=l[k]*np.random.rand(2,N)
    point,=ax.plot(x[0],x[1],'yo')
    angu0=2*np.pi*(np.random.rand(N))
    v=v0*np.array([np.cos(angu0), np.sin(angu0)])
    
    #Modelización del choque frente a las paredes de la caja y cálculo de la presión
    #a partir de ellos.
    for i in range(npasos):
        x=x+v*dt
        presiontodas[i]=0
        for j in range(N):
            if x[0,j] <=0:
                if v[0,j]<0:
                    v[0,j]=-v[0,j]
                    presiontodas[i]+=0.5*m*np.abs(v[0,j])/l[k]/dt
            if x[0,j]>=l[k]:
                if v[0,j]>0:
                    v[0,j]=-v[0,j]
                    presiontodas[i]+=0.5*m*np.abs(v[0,j])/l[k]/dt
            if x[1,j] <=0:
                if v[1,j]<0:
                    v[1,j]=-v[1,j]
                    presiontodas[i]+=0.5*m*np.abs(v[1,j])/l[k]/dt
            if x[1,j]>=l[k]:
                if v[1,j]>0:
                    v[1,j]=-v[1,j]
                    presiontodas[i]+=0.5*m*np.abs(v[1,j])/l[k]/dt
                
        if i % int(npasos/pasosrepre)==0:
            presion[int(i/pasosrepre)]=np.mean(presiontodas[i-pasosrepre:i])
            
        points_tree=spatial.cKDTree(x.T)
        pairs=points_tree.query_pairs(epsilon)
            
        for ipair in pairs:
            v[:,ipair[0]],v[:,ipair[1]]=choque(x[:,ipair[1]]-x[:,ipair[0]],v[:,ipair[0]],v[:,ipair[1]])
        
        if i % pasosrepre ==0:
            point.set_data(x[0],x[1]) 
                
            plt.pause(pausa)
    
    presion[0]=0
    presionmedia=np.mean(presion)
    presion2[k]=presionmedia

print(presion2)


#Función para determinar el ajuste lineal de la representación
def ajlineal(x,m):
    return m*x

#Representación de la presión frente al inverso del área
coef1,coef2=so.curve_fit(ajlineal,areainv,presion2)
plt.figure()
plt.grid()
X=np.linspace(0.00,0.012,400)
plt.plot(areainv,presion2,'rx')
plt.plot(X,coef1[0]*X,label='Ajuste lineal')
plt.xlim(0)
plt.ylim(0)
plt.xlabel('$Área^{-1}$')
plt.ylabel('Presión')
plt.title('P vs $Área^{-1}$')
plt.legend()
plt.savefig('presarea1')
plt.show()    

print('Pendiente:'+str(coef1[0]))

#Representación de la presión frente al área
'''
plt.figure()
plt.title('Presión vs área')
plt.grid()
plt.xlabel('Área')
plt.ylabel('Presión')
plt.plot(area1,presion2,'ro')
plt.savefig('presarea')
plt.show()
'''