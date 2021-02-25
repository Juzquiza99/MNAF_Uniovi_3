# -*- coding: utf-8 -*-
"""
Editor de Spyder

Este es un archivo temporal
"""
'''
PRÁCTICA 2: PROPAGACIÓN DE ONDAS EM
c=3E8
separación en mallado en eje x dx=10 nm
puntos mallado: 1001
paso temporal dt: c(dt/dx)=0.5
numero pasos t: 5000
pasos entre reps:10
pausa entre reps: 0.01
'''

import numpy as np
import matplotlib.pyplot as plt

#en primer lugar vamos con la propagación de la onda en el vacío, a partir de un pulso
#gaussiano

#Constantes y coeficientes
c=3e8
nx=1001 #puntosmallado
Eo=1
dx=10e-9 #nm
dxp=400e-9 #nm
npasos=5000
dt=dx/(2*c)
dtp=dxp/c
pasosrepre=10
pausa=0.01
ptoinicial=501
x=np.linspace(0,(nx-1)*dx,nx)

#Campo eléctrico y magnético
E=np.zeros(nx) 
H=np.zeros(nx)


#Representación de los campos
fig=plt.figure(figsize=(6,6))
ax=fig.add_subplot(111) #Eje x
plt.title('Propagación de ondas EM en el vacío')
pele,pmag=ax.plot(x,E,'r',x,H,'g') 
ax.set_xlim((0,(nx-1)*dx)) #Límites ejes
ax.set_ylim((-1.5,1.5))

#Actualización mutua de ambos campos a partir del valor del otro, según avanza
#el tiempo
for j in range(npasos):
    for i in range(1,nx):
        E[i]=E[i]-0.5*(H[i]-H[i-1])  
    E[ptoinicial]=Eo*np.exp(-0.5*((j*dt-5*dtp)/(dtp))**2)
    
    for k in range(nx-1):   
        H[k]=H[k]-0.5*(E[k+1]-E[k])
    
    if np.mod(j,pasosrepre)==0:
        pele.set_data(x,E)
        pmag.set_data(x,H)
            
        plt.pause(pausa)

plt.show()