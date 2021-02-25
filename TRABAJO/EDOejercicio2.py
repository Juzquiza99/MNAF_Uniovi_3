# -*- coding: utf-8 -*-

import numpy as np 
import matplotlib.pyplot as plt 

###############################################################################
# Implementacion del metodo de Euler explicito para resolver
# la ecuacion Lotka-Volterra, dos ecuaciones del tipo
# u' = u(alpha-beta*u)
###############################################################################

###############################################################################
##### Intervalo temporal
###############################################################################
t0 = 0
T = 50
dt = 1.e-3

###############################################################################
##### Termino de reaccion, dato inicial y solucion exacta
###############################################################################
alpha = np.array([1,-0.5])
beta=np.array(([0,0.1],[-0.05,0]))
u01=8.
u02=1.
u0=np.array([u01,u02])
us=np.linalg.solve(beta,alpha) #Punto de equilibrio no trivial

###############################################################################
##### Inicializacion
###############################################################################
u1 = u01                         # u en cada t
u_time1 = u01                    # array que guarda todos los valores de u
u2=u02
u_time2=u02

###############################################################################
##### Bucle temporal
###############################################################################
t = t0
while t < T:
    t += dt
    reaccion1 = u1*(alpha[0]-beta[0,0]*u1-beta[0,1]*u2)
    reaccion2= u2*(alpha[1]-beta[1,0]*u1-beta[1,1,]*u2)
    u1 += dt*reaccion1
    u2 += dt*reaccion2
    u_time1 = np.append(u_time1, u1)
    u_time2 = np.append(u_time2, u2)
time = np.linspace(t0,t,len(u_time1))    

###############################################################################
##### Salidas
###############################################################################

# Plotting
fig = plt.figure()
axes = fig.add_axes([0.1,0.1,0.8,0.8]) 
axes.plot(time, u_time1, label = 'Presa')
axes.plot(time, u_time2, label = 'Depredador')
axes.plot(time,us[0]*np.ones(len(u_time1)),'--',label='Equilibrio presa')
axes.plot(time, us[1]*np.ones(len(u_time2)),'-.',label='Equilibrio depredador')
axes.legend(loc=1)
axes.set_title(u'Soluciones de depredador-presa')
plt.show()
    
fig2 = plt.figure()
axes2 = fig2.add_axes([0.1,0.1,0.8,0.8]) 
axes2.plot(u_time1,u_time2, label = 'Órbita')
axes2.plot(u01,u02,'ro',label='Inicio')
axes2.plot(us[0],us[1],'r*',label='Equilibrio')
axes2.legend(loc=1)
axes2.set_title(u'Plano de fases depredador-presa')
plt.show()
    
