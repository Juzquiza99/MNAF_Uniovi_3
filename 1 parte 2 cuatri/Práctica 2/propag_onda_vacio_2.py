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
ptoinicial=251
coefdiele=np.zeros(nx) #epsilon
pared=501
sigma=np.zeros(nx) #conductividad
epsilon0=8.854e-12
cte=np.zeros(nx) #unos coeficientes
ca=np.zeros(nx)
cb=np.zeros(nx)
x=np.linspace(0,(nx-1)*dx,nx)
E=np.zeros(nx)
H=np.zeros(nx)


#primer medio: vacío; segundo medio: epsilonr=4
fig=plt.figure(figsize=(6,6))
ax=fig.add_subplot(111) #Eje x
plt.title('Propagación de ondas EM en el vacío')
pele,pmag=ax.plot(x,E,'r',x,H,'g') 
ax.set_xlim((0,(nx-1)*dx)) #Límites ejes
ax.set_ylim((-1.5,1.5))
ax.axvline(x=x[pared],color='k')
epsilonr1=1
epsilonr2=4
sigma1=0
sigma2=4000
coefdiele[0:pared]=epsilonr1
coefdiele[pared:nx]=epsilonr2
sigma[0:pared]=sigma1
sigma[pared:nx]=sigma2
tub1=np.zeros(2)
tub2=np.zeros(np.round(2*np.sqrt(epsilonr2)).astype(int))
print(tub2)


#debido a la diferencia de los índices de refracción a través del coef diele, la
#velocidad de propagación de la luz es diferente, por ello, hay que ajustar los
#pasos temporales
for j in range(npasos):
    
    for i in range(nx):
        cte[i]=(sigma[i]*dt)/(2*coefdiele[i]*epsilon0)
        ca[i]=(1-cte[i])/(1+cte[i])
        cb[i]=1/(2*coefdiele[i]*(1+cte[i]))
        E[i]=ca[i]*E[i]-cb[i]*(H[i]-H[i-1])
    
    #Absorción del rebote de las paredes
    E[0]=tub1[1]    
    tub1[1]=tub1[0]
    tub1[0]=E[1]

    E[-1]=tub2[-1]

    tub2[1:]=tub2[:-1]
    tub2[0]=E[-2]
        
    E[ptoinicial]+=Eo*np.exp(-0.5*((j*dt-5*dtp)/(dtp))**2)
        
        
    for k in range(nx-1):   
        H[k]=H[k]-0.5*(E[k+1]-E[k])
    
    if np.mod(j,pasosrepre)==0:
        pele.set_data(x,E)
        pmag.set_data(x,H)
            
        plt.pause(pausa)

plt.show()