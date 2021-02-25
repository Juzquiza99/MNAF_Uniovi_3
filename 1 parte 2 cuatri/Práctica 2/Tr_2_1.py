# -*- coding: utf-8 -*-
"""
Created on Sun Apr 12 12:47:27 2020

@author: javie
"""

#Autor: Javier Uzquiza López

#PROPAGACIÓN EN 2 DIMENSIONES

'''
Indicaciones de uso del programa:
    si se desea modificar los coeficientes de la permitividad eléctrica para los
    medios se cambian los valores de epsilonr1 y epsilonr2.
    De igual manera, cualquier otro parámetro referente a la frecuencia del pulso
    o velocidad de representación son susceptibles de ser modificados.
'''
import numpy as np
import matplotlib.pyplot as plt

#Constantes y parámetros utilizados en la modelización
c=3e8 #velocidad de la luz en el vacío
dx=40e-9
dxp=400e-9 #anchura pulso
dt=dx/(2*c)
dtp=dxp/c
nx=401 #malla xy
ny=401
Eo=1
dx=10e-9
npasos=4000
pausa=0.01
x=np.linspace(0,(nx-1)*dx,nx)
y=np.linspace(0,(ny-1)*dx,ny)
pasosrepre=10
Ez=np.zeros((nx,ny))
Hx=np.zeros((nx,ny))
Hy=np.zeros((nx,ny))
pared=201 #posición de la pared

epsilon0=8.854e-12 #permitividad eléctrica en el vacío

fig=plt.figure(figsize=(6,6))
ax=fig.add_subplot(111)


levels=np.linspace(-0.1,0.1,21)
xx,yy=np.meshgrid(x,y)
cs=ax.contourf(xx,yy,np.clip(Ez,-0.1,0.1),levels,cmap='seismic')
bar=plt.colorbar(cs)
tub1=np.zeros((2,ny))
tub2=np.zeros((2,ny))
tub3=np.zeros((2,ny))
tub4=np.zeros((2,ny))

#Coeficientes de la permitividad eléctrica para los dos medios
epsilonr1=2
epsilonr2=1

#Conductividad de los medios
sigma1=0
sigma2=4000
coefdiele=np.array([epsilonr1,epsilonr2])
sigma=np.array([sigma1,sigma2])

#Coeficientes que determinan la propagación
cte=(sigma*dt)/(2*coefdiele*epsilon0)
ca=(1-cte)/(1+cte)
cb=1/(2*coefdiele*(1+cte))

#Relación entre campo eléctrico y magnético
for j in range(npasos): 
    Ez[1:,1:pared]=ca[0]*Ez[1:,1:pared]+cb[0]*(Hy[1:,1:pared]-Hy[:-1,1:pared])-cb[0]*(Hx[1:,1:pared]-Hx[1:,:pared-1])
    Ez[1:,pared:]=ca[1]*Ez[1:,pared:]+cb[1]*(Hy[1:,pared:]-Hy[:-1,pared:])-cb[1]*(Hx[1:,pared:]-Hx[1:,pared-1:-1])
    
    #Frente de ondas sinusoidal situado en el  con pendiente de 45º
    for i in range(50):
        Ez[50-i,i]=Eo*np.sin((2*np.pi/dtp)*j*dt)
    
    
    #Añadimos condiciones de contorno absorbentes (que no rebote la onda en las paredes)
    Ez[0,:]=tub1[1,:]    
    tub1[1,:]=tub1[0,:]
    tub1[0,:]=Ez[1,:]

    Ez[-1,:]=tub2[1,:]
    tub2[1:,:]=tub2[0,:]
    tub2[0,:]=Ez[-2,:]
    
    Ez[:,0]=tub3[-1,:]
    tub3[1,:]=tub3[0,:]
    tub3[0,:]=Ez[:,1]
    
    Ez[:,-1]=tub4[1,:]
    tub4[1:,:]=tub4[0,:]
    tub4[0,:]=Ez[:,-2]
    
    Hx[:,:-1]=Hx[:,:-1]-0.5*(Ez[:,1:]-Ez[:,:-1])
    Hy[:-1,:]=Hy[:-1,:]+0.5*(Ez[1:,:]-Ez[:-1,:])
        

    #Representación de la propagación a lo largo del tiempo
    if np.mod(j,pasosrepre)==0:
        ax.cla()
        ax.axvline(x=x[pared],color='k')
        ax.contourf(xx,yy,np.clip(Ez,-0.1,0.1),levels,cmap='seismic')
        ax.set_title(r'Reflexión y refracción ${\varepsilon}_1=2$, ${\varepsilon}_2=1$')
        ax.ticklabel_format(style='sci',axis='both',scilimits=(-6,-6))
        plt.pause(pausa)
plt.show()