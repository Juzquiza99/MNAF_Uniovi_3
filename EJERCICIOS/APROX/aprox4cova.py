# -*- coding: utf-8 -*-
"""
Created on Fri Nov  8 16:48:09 2019

@author: UO264117
"""

import numpy as N
from scipy.integrate import quad
import numpy.linalg as LA
import matplotlib.pyplot as plt
import scipy.optimize as SO
#polinomio de tercer grado, exponencial, potencial, crecimiento

#FUNCIÓN 1

X1=N.array([0.75,2,2.5,4,6,8,8.5])
Y1=N.array([0.8,1.3,1.2,1.6,1.7,1.8,1.7])

X=N.linspace(N.min(X1),N.max(X1),51)

#EXPONENCIAL - linealizo el problema, esto me va a dar una recta y=lna+b*x
exp1=N.polyfit(X1,N.log(Y1),1)
b1=N.exp(exp1[0])
a1=exp1[1]

#Aproximacion por un polinomio de tercer grado
pol1=N.polyfit(X1,Y1,3) # EL 3 ES PARA QUE SEA DE GRADO 3

#APROXIMACION POTENCIAL
pot1=N.polyfit(N.log(X1),N.log(Y1),1)
#calcula la potencial con el curvefit
funcionpot1=lambda x,a,b: a*x**b
coef_pot1,cov_pot1=SO.curve_fit(funcionpot1,X1,Y1)

#aproximacion por crecimineto
crec1=N.polyfit(1./X1,1./Y1,1)


#Vamos a hacer tambien exponencial, potencial y crecimiento con el curvefit
funcionexp1=lambda x,a,b:a*N.exp(b*x)
coef_exp1,cov_exp1=SO.curve_fit(funcionexp1,X1,Y1)# el curve fit lo que hace es
#tu le das la funcion a la que quieres aproximar ciertos puntos, el soporte
#entonces le pasas esa funcion y x1,y1(que es el soporte), y te lo aproxima

plt.figure()
plt.plot(X1,Y1,'bo',label='datos')
plt.plot(X,pol1[3]+pol1[2]*X+pol1[1]*(X**2)+pol1[0]*(X**3),label='Polinomio de grado 3')
#plt.plot(X,N.polyval(pol1,X),label='Polinome grado 3') #lo mismo pero con polyval que lo hace solo
plt.plot(X,N.exp(N.polyval(exp1,X)),label='Exponencial')
plt.plot(X,funcionexp1(X,*coef_exp1),label='Exponencial CURVE_FIT')
#el asterisco lo que hace es que coef_exp1 te da dos coeficientes a y b
#entonces en vez de poner cpef_exp1[0],coef_exp1[1], al poner
#el asterisco ya te lo desglosa solo
plt.plot(X,1./(N.polyval(crec1,1./X)),label='Crecimiento')
plt.plot(X,N.exp(N.polyval(pot1,N.log(X))),label='Potencial')
plt.plot(X,funcionpot1(X,*coef_pot1),label='Potencial CURVE_FIT')
plt.title('Linealizacion', fontsize=20)
plt.grid()
plt.legend()
plt.show()
