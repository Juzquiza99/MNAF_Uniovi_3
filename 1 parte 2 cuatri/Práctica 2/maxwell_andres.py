# -*- coding: utf-8 -*-
"""
Created on Sun Apr 12 12:06:13 2020

@author: javie
"""

import numpy as np
import matplotlib.pyplot as plt
import scipy.spatial as spatial

 

c = 3E8
deltax  = 10E-9
deltat = deltax/(2*c)
deltaxp = np.array([40E-9,60E-9,80E-9])

 

npuntos = 401
npasos = 2000
pasosrep = 10
pausa = 0.01
origen = 0
deltatp = deltaxp/c
x = np.linspace(0,(npuntos-1)*deltax,npuntos)
y = np.linspace(0,(npuntos-1)*deltax,npuntos)
xx,yy = np.meshgrid(x,y)
levels = np.linspace(-0.1,0.1,21)
fig=plt.figure(figsize=(6,6))
ax1=fig.add_subplot(121)
ax1.set_ylim(0,1e-6)
ax2=fig.add_subplot(122)
ax2.set_ylim((0,1e-6))
ax2.ticklabel_format(style='sci',axis='both',scilimits=(-6,-6))
Ez = np.zeros((npuntos,npuntos))
Hx = np.zeros((npuntos,npuntos))
Hy = np.zeros((npuntos,npuntos))
n = 201
n1 = 101
epsilon1=1
epsilon2=1
epsilon = np.zeros((npuntos,npuntos))
epsilon[:,:n] = epsilon1
epsilon[:,n:] = epsilon1
sigma1 = 0
sigma2 = 0
epsilon0 = 8.854e-12
sigma = np.zeros((npuntos,npuntos))
sigma[:,:n] = sigma1
sigma[:,n:] = sigma2
ctc = sigma*deltat/(2*epsilon0*epsilon)
ca = (1-ctc)/(1+ctc)
cb = 0.5/(epsilon*(1+ctc))
pared = np.zeros(npuntos)
pared[180:188] = 1
pared[212:220] = 1
campos=np.zeros((len(deltaxp),npuntos))

 

cs = ax1.contourf(xx,yy,np.clip(Ez,-0.1,0.1),levels,cmap='seismic')
bar = plt.colorbar(cs)
tubo1 = np.zeros((2,npuntos))
tubo2 = np.zeros((2,npuntos))
tubo3 = np.zeros((2,npuntos))
tubo4 = np.zeros((2,npuntos))

 

repreE,=ax2.plot(y,Ez[-1,:]*np.conj(Ez[-1,:]),'g')

 

for k in range(len(deltaxp)):
    for j in range (0,npasos):
        Ez[1:,1:] = Ez[1:,1:]+0.5*(Hy[1:,1:]-Hy[:-1,1:])-0.5*(Hx[1:,1:]-Hx[1:,:-1])
        Ez[n,n1] = np.sin(deltat*j/deltatp[k])
        Ez[:,n] = pared*Ez[:,n]
        Ez[0,:] = tubo1[1,:]
        tubo1[1,:] = tubo1[0,:]
        tubo1[0,:]=Ez[1,:]
        
        Ez[-1,:] = tubo2[1,:]
        tubo2[1,:] = tubo2[0,:]
        tubo2[0,:]=Ez[-2,:]
        
        Ez[:,0] = tubo3[1,:]
        tubo3[1,:] = tubo3[0,:]
        tubo3[0,:]=Ez[:,1]
        
        Ez[:,-1] = tubo4[1,:]
        tubo4[1,:] = tubo4[0,:]
        tubo4[0,:]=Ez[:,-2]
        
        Hx[:,:-1] = Hx[:,:-1]-0.5*(Ez[:,1:]-Ez[:,:-1])
        Hy[:-1,:] = Hy[:-1,:]+0.5*(Ez[1:,:]-Ez[:-1,:])
        campos[k]+=Ez[:,-1]**2
        if np.mod(j,pasosrep)==0:
            repreE.set_data(y,Ez[:,-1]**2/377)
            ax1.cla()
            ax1.axvline(x=x[n],color='k')
            ax1.ticklabel_format(style='sci',axis='both',scilimits=(-6,-6))
            ax1.contourf(xx,yy,np.clip(Ez,-0.1,0.1),levels,cmap='seismic')
            plt.pause(pausa)

 

plt.figure()
plt.plot(x,campos[0]/np.amax(campos[0]),label='$f_1$')
plt.plot(x,campos[1]/np.amax(campos[1]),label='$f_2 < f_1$')
plt.plot(x,campos[2]/np.amax(campos[2]),label='$f_3 < f_2$')
plt.ticklabel_format(style='sci',axis='both',scilimits=(-6,-6))
plt.xlabel('x (m)')
plt.ylabel('$\propto$ I ($W/m^2$)')
plt.title('Intensidad en la pantalla')
plt.legend()
plt.show()