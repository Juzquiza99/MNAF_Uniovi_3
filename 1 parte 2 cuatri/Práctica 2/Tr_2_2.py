# -*- coding: utf-8 -*-
"""
Created on Sun Apr 12 19:27:49 2020

@author: javie
"""

#Autor: Javier Uzquiza López

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
Z0=377 #Impedancia del vacío
dx=10e-9
dt=dx/(2*c)
#Anchuras de los pulsos para el estudio de la dependencia de la frecuencia
dxp=np.array([4e-8,6.5e-8,9e-8])
nptos=401
npasos=1000
pasosrepre=10
pausa=0.01
dtp=dxp/c
x=np.linspace(0,(nptos-1)*dx,nptos)
y=np.linspace(0,(nptos-1)*dx,nptos)

#Representación
fig=plt.figure(figsize=(6,6))
ax1=fig.add_subplot(121)
ax1.set_ylim(0,1e-6)
ax2=fig.add_subplot(122)
ax2.set_ylim((0,1e-6))
ax2.ticklabel_format(style='sci',axis='both',scilimits=(-6,-6))

#Campo eléctrico y magnético
Ez=np.zeros((nptos,nptos))
Hx=np.zeros((nptos,nptos))
Hy=np.zeros((nptos,nptos))
#posición de la fuente emisora
pmedio=201
fuentex=101

#Coeficientes de la permitividad eléctrica en el vacío para los dos medios
epsilonr1=1
epsilonr2=1
coefdiele=np.zeros((nptos,nptos))
coefdiele[:,:pmedio]=epsilonr1
coefdiele[:,pmedio:]=epsilonr1

#Conductividad
sigma1=0
sigma2=0

epsilon0=8.854e-12 #permitividad del vacío
sigma=np.zeros((nptos,nptos))
sigma[:,:pmedio]=sigma1
sigma[:,pmedio:]=sigma2

#Coeficientes que determinan la propagación
ctc=sigma*dt/(2*epsilon0*coefdiele)
ca=(1-ctc)/(1+ctc)
cb=0.5/(coefdiele*(1+ctc))

#Configuración de la pared con los agujeros. El campo se anula en contacto con
#la pared, mientras que en los agujeros el campo continua de forma normal.
pared=np.zeros(nptos)
pared[180:187]=1
pared[213:220]=1
intesfre=np.zeros((len(dxp),nptos))  #Intensidades para pulsos de distintas anchuras

#Configuración de la representación
xx,yy=np.meshgrid(x,y)
levels=np.linspace(-0.1,0.1,21)
cs=ax1.contourf(xx,yy,np.clip(Ez,-0.1,0.1),levels,cmap='seismic')
bar=plt.colorbar(cs)

#Puntero que hará referencia a la intensidad en tiempo real en la pantalla
repreint,=ax2.plot(y,Ez[-1,:]*np.conj(Ez[-1,:]))


tub1=np.zeros((2,nptos))
tub2=np.zeros((2,nptos))
tub3=np.zeros((2,nptos))
tub4=np.zeros((2,nptos))

#Se añaden condiciones de contorno absorbentes para evitar el rebote de la onda
#con las paredes y se introducen las expresiones que rigen la propagación de los
#campos eléctrico y magnético a lo largo del tiempo y el espacio.
for k in range(len(dxp)):
    for j in range (0,npasos):
        Ez[1:,1:]=Ez[1:,1:]+0.5*(Hy[1:,1:]-Hy[:-1,1:])-0.5*(Hx[1:,1:]-Hx[1:,:-1])
        Ez[pmedio,fuentex]=np.sin(dt*j/dtp[k])
        Ez[:,pmedio]=pared*Ez[:,pmedio]
        Ez[0,:]=tub1[1,:]
        tub1[1,:]=tub1[0,:]
        tub1[0,:]=Ez[1,:]
        
        Ez[-1,:]=tub2[1,:]
        tub2[1,:]=tub2[0,:]
        tub2[0,:]=Ez[-2,:]
        
        Ez[:,0]=tub3[1,:]
        tub3[1,:]=tub3[0,:]
        tub3[0,:]=Ez[:,1]
        
        Ez[:,-1]=tub4[1,:]
        tub4[1,:]=tub4[0,:]
        tub4[0,:]=Ez[:,-2]
        
        Hx[:,:-1]=Hx[:,:-1]-0.5*(Ez[:,1:]-Ez[:,:-1])
        Hy[:-1,:]=Hy[:-1,:]+0.5*(Ez[1:,:]-Ez[:-1,:])
        intesfre[k]+=Ez[:,-1]**2
        
        #Representación de la intensidad en la pantalla y del pulso en el espacio
        if np.mod(j,pasosrepre)==0:
            repreint.set_data(y,Ez[:,-1]**2/Z0)    
            ax2.set_title('Intensidad en la pantalla')
            ax1.cla()
            ax1.axvline(x=x[pmedio],color='k') #Pared
            ax1.ticklabel_format(style='sci',axis='both',scilimits=(-6,-6))
            ax1.contourf(xx,yy,np.clip(Ez,-0.1,0.1),levels,cmap='seismic')
            ax1.set_title('Pulso en el espacio')
            plt.pause(pausa)

 
#Representación de la intensidad recibida para los pulsos de distintas frecuencias
plt.figure()
plt.grid()
#Mostramos los patrones de interferencia y difracción normalizados
plt.plot(y,intesfre[0]/np.amax(intesfre[0]),label='Altas frecuencias')
plt.plot(y,intesfre[1]/np.amax(intesfre[1]),label='Medias frecuencias')
plt.plot(y,intesfre[2]/np.amax(intesfre[2]),label='Bajas frecuencias')
plt.ticklabel_format(style='sci',axis='both',scilimits=(0,-6)) #Orden de las unidades de los ejes
plt.xlabel('y (m)')
plt.ylabel('I / Imáx')
plt.title('Intensidad recibida en la pantalla')
plt.legend()
plt.show()
