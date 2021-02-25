# -*- coding: utf-8 -*-
"""
Editor de Spyder

Este es un archivo temporal
"""

#PROPAGACIÓN EN 2 DIMENSIONES

#mallado 401 X 401
#pulso: 40 nm
#mapa de calor


import numpy as np
import matplotlib.pyplot as plt

#Constantes y parámetros utilizados en la modelización
c=3e8
dx=10e-9
dxp=40e-9 #anchura pulso
dt=dx/(2*c)
dtp=dxp/c
nx=401
ny=401
inix,iniy=201,101
Eo=1
dx=10e-9
npasos=5000
pausa=0.01
x=np.linspace(0,(nx-1)*dx,nx)
y=np.linspace(0,(ny-1)*dx,ny)
pasosrepre=10
Ez=np.zeros((nx,ny))
Hx=np.zeros((nx,ny))
Hy=np.zeros((nx,ny))
pared=201
epsilon0=8.854e-12

#Representación de la figura
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

#permitividad y cinductividad
epsilonr1=1
epsilonr2=4
sigma1=0
sigma2=4000
coefdiele=np.array([epsilonr1,epsilonr2])
sigma=np.array([sigma1,sigma2])
cte=(sigma*dt)/(2*coefdiele*epsilon0)
ca=(1-cte)/(1+cte)
cb=1/(2*coefdiele*(1+cte))


#Se añaden condiciones de contorno absorbentes para evitar el rebote de la onda
#con las paredes y se introducen las expresiones que rigen la propagación de los
#campos eléctrico y magnético a lo largo del tiempo y el espacio.
for j in range(npasos):
    
    Ez[1:,1:pared]=ca[0]*Ez[1:,1:pared]+cb[0]*(Hy[1:,1:pared]-Hy[:-1,1:pared])-cb[0]*(Hx[1:,1:pared]-Hx[1:,:pared-1])
    Ez[1:,pared:]=ca[1]*Ez[1:,pared:]+cb[1]*(Hy[1:,pared:]-Hy[:-1,pared:])-cb[1]*(Hx[1:,pared:]-Hx[1:,pared-1:-1])
    Ez[inix,iniy]=Eo*np.exp(-0.5*((j*dt-5*dtp)/(dtp))**2)
    
    
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
        

     
    if np.mod(j,pasosrepre)==0:
        ax.cla()
        ax.axvline(x=x[pared],color='k')
        ax.contourf(xx,yy,np.clip(Ez,-0.1,0.1),levels,cmap='seismic')
        plt.pause(pausa)
plt.show()


