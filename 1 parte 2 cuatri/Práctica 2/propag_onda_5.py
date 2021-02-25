# -*- coding: utf-8 -*-
"""
Editor de Spyder

Este es un archivo temporal
"""

#EXPERIMENTO DE LA DOBLE RENDIJA

#mallado 401 X 401
#pulso: 40 nm
#mapa de calor


import numpy as np
import matplotlib.pyplot as plt

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

fig=plt.figure(figsize=(6,6))
ax=fig.add_subplot(111)


levels=np.linspace(-0.1,0.1,21)
xx,yy=np.meshgrid(x,y)
cs=ax.contourf(xx,yy,np.clip(Ez,-0.1,0.1),levels,cmap='seismic')
bar=plt.colorbar(cs)


for j in range(npasos):
    
    Ez[1:,1:]=0.5*Ez[1:,1:]+0.5*(Hy[1:,1:]-Hy[:-1,1:])-0.5*(Hx[1:,1:]-Hx[1:,:-1])
    Ez[inix,iniy]=Eo*np.sin((2*np.pi/dtp)*j*dt)
    

    Hx[:,:-1]=Hx[:,:-1]-0.5*(Ez[:,1:]-Ez[:,:-1])
    Hy[:-1,:]=Hy[:-1,:]+0.5*(Ez[1:,:]-Ez[:-1,:])
        

     
    if np.mod(j,pasosrepre)==0:
        ax.cla()
        ax.axvline(x=x[pared],color='k')
        ax.contourf(xx,yy,np.clip(Ez,-0.1,0.1),levels,cmap='seismic')
        plt.pause(pausa)
plt.show()
