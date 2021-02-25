# -*- coding: utf-8 -*-

import numpy as np 
import matplotlib.pyplot as plt 

###############################################################################
# Implementacion del metodo de Euler explicito para resolver
# la ecuacion logística
# u' = u(alpha-beta*u)
###############################################################################

###############################################################################
##### Intervalo temporal
###############################################################################
t0 = 0
T = 3
dt = 5.e-2

###############################################################################
##### Termino de reaccion, dato inicial y solucion exacta
###############################################################################
alpha = 2.
r=alpha
beta=1.
K=alpha/beta #Punto de equilibrio no trivial
u0 = K+0.5
u_exacta = lambda t: K*u0/(u0+(K-u0)*np.exp(-r*t))

###############################################################################
##### Inicializacion
###############################################################################
u = u0                         # u en cada t
u_time = u0                    # array que guarda todos los valores de u

###############################################################################
##### Bucle temporal
###############################################################################
t = t0
while t < T:
    t += dt
    reaccion = u*(alpha-beta*u)
    u += dt*reaccion
    u_time = np.append(u_time, u)
time = np.linspace(t0,t,len(u_time))    
###############################################################################    
##### Error relativo respecto exacta   
###############################################################################
exacta = u_exacta(time)
error_relativo = np.linalg.norm(u_time-exacta)/ np.linalg.norm(exacta)

###############################################################################
##### Salidas
###############################################################################
# Consola
print(u'Error relativo = ', error_relativo)
# Plotting
fig = plt.figure()
axes = fig.add_axes([0.1,0.1,0.8,0.8]) 
axes.plot(time, u_time, label = 'Aproximada')
axes.plot(time, exacta, label = 'Exacta')
axes.set_title(u'Soluciones de la ecuación logística')
axes.legend(loc=2)
    
