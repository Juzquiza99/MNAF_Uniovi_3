# -*- coding: utf-8 -*-
"""
Created on Fri Nov  8 17:00:56 2019

@author: UO264982
"""

import numpy as np
import numpy.linalg as la
import matplotlib.pyplot as plt
import scipy.optimize as SO
#EJEMPLO 9 polinomio de tercer grado, exponencial, potencial, crecimiento
    
X1=np.array([0.75,2,2.5,4,6,8,8.5])
Y1=np.array([0.8,1.3,1.2,1.6,1.7,1.8,1.7])
X2=np.array([2.5,3.5,5,6,7.5,10,12.5,15,17.5,20])
Y2=np.array([7,5.5,3.9,3.6,2.1,2.8,2.6,2.4,2.3,2.3])
X3=np.array([0.4,0.8,1.2,1.6,2.0,2.3])
Y3=np.array([0.75,1.0,1.4,2.0,2.7,3.75])
X4=np.array([126,365,506,527,562,703])
Y4=np.array([0.5,1.3,2,4.5,6,8.5])

coef11=np.polyfit(X1,Y1,3) #grado 3
coef21=np.polyfit(X1,np.log(Y1),1) #exp
coef31=np.polyfit(np.log(X1),np.log(Y1),1) #poten
coef41=np.polyfit(1/X1,1/Y1,1) #crecimiento

#calcula la potencial con el curvefit
funcionpot1=lambda x,a,b: a*x**b
coef_pot1,cov_pot1=SO.curve_fit(funcionpot1,X1,Y1)
funcionexp1=lambda x,a,b:a*np.exp(b*x)
coef_exp1,cov_exp1=SO.curve_fit(funcionexp1,X1,Y1)
funlogis=lambda x,a,b,c,d: a/(1+np.exp(b*x-c) +d)
coef_logis1,cov_logis1=SO.curve_fit(funlogis,X1,Y1)

X = np.linspace(X1[0],X1[-1],201)

print('[X1,Y1]:')
plt.figure()
plt.plot(X1,Y1,'bo',label='datos')
plt.plot(X,np.polyval(coef11,X),label='poly3')
plt.plot(X,np.exp(np.polyval(coef21,X)),label='exp')
plt.plot(X,np.exp(np.polyval(coef31,np.log(X))),label='potencial')
plt.plot(X,1./np.polyval(coef41,1./X),label='crecimiento')
plt.plot(X,funcionexp1(X,*coef_exp1),label='Exponencial CURVE_FIT')
plt.plot(X,funcionpot1(X,*coef_pot1),label='Potencial CURVE_FIT')
plt.plot(X,funlogis(X,*coef_logis1),label='Logística')
plt.grid()
plt.legend()
plt.show()


X = np.linspace(X2[0],X2[-1])
coef12=np.polyfit(X2,Y2,3) #grado 3
coef22=np.polyfit(X2,np.log(Y2),1) #exp
coef32=np.polyfit(np.log(X2),np.log(Y2),1) #poten
coef42=np.polyfit(1/X2,1/Y2,1) #crecimiento

#calcula la potencial con el curvefit
funcionpot1=lambda x,a,b: a*x**b
coef_pot2,cov_pot2=SO.curve_fit(funcionpot1,X2,Y2)
funcionexp1=lambda x,a,b:a*np.exp(b*x)
coef_exp2,cov_exp2=SO.curve_fit(funcionexp1,X2,Y2)
coef_logis2,cov_logis2=SO.curve_fit(funlogis,X2,Y2)

print('[X2,Y2]:')
plt.figure()
plt.plot(X2,Y2,'bo',label='datos')
plt.plot(X,np.polyval(coef12,X),label='poly3')
plt.plot(X,np.exp(np.polyval(coef22,X)),label='exp')
plt.plot(X,np.exp(np.polyval(coef32,np.log(X))),label='potencial')
plt.plot(X,1./np.polyval(coef42,1./X),label='crecimiento')
plt.plot(X,funcionexp1(X,*coef_exp2),label='Exponencial CURVE_FIT')
plt.plot(X,funcionpot1(X,*coef_pot2),label='Potencial CURVE_FIT')
plt.plot(X,funlogis(X,*coef_logis2),label='Logística')
plt.grid()
plt.legend()
plt.show()


X = np.linspace(X3[0],X3[-1])
coef13=np.polyfit(X3,Y3,3) #grado 3
coef23=np.polyfit(X3,np.log(Y3),1) #exp
coef33=np.polyfit(np.log(X3),np.log(Y3),1) #poten
coef43=np.polyfit(1/X3,1/Y3,1) #crecimiento

#calcula la potencial con el curvefit
funcionpot1=lambda x,a,b: a*x**b
coef_pot3,cov_pot3=SO.curve_fit(funcionpot1,X3,Y3)
funcionexp1=lambda x,a,b:a*np.exp(b*x)
coef_exp3,cov_exp3=SO.curve_fit(funcionexp1,X3,Y3)
coef_logis3,cov_logis3=SO.curve_fit(funlogis,X3,Y3)

print('[X3,Y3]:')
plt.figure()
plt.plot(X3,Y3,'bo',label='datos')
plt.plot(X,np.polyval(coef13,X),label='poly3')
plt.plot(X,np.exp(np.polyval(coef23,X)),label='exp')
plt.plot(X,np.exp(np.polyval(coef33,np.log(X))),label='potencial')
plt.plot(X,1./np.polyval(coef43,1./X),label='crecimiento')
plt.plot(X,funcionexp1(X,*coef_exp3),label='Exponencial CURVE_FIT')
plt.plot(X,funcionpot1(X,*coef_pot3),label='Potencial CURVE_FIT')
plt.plot(X,funlogis(X,*coef_logis3),label='Logística')

plt.grid()
plt.legend()
plt.show()


X = np.linspace(X4[0],X4[-1])
coef14=np.polyfit(X4,Y4,3) #grado 3
coef24=np.polyfit(X4,np.log(Y4),1) #exp
coef34=np.polyfit(np.log(X4),np.log(Y4),1) #poten
coef44=np.polyfit(1/X4,1/Y4,1) #crecimiento

#calcula la potencial con el curvefit
funcionpot1=lambda x,a,b: a*x**b
coef_pot4,cov_pot4=SO.curve_fit(funcionpot1,X4,Y4)
funcionexp1=lambda x,a,b:a*np.exp(b*x)
coef_exp4,cov_exp4=SO.curve_fit(funcionexp1,X4,Y4)
coef_logis4,cov_logis4=SO.curve_fit(funlogis,X4,Y4)

print('[X4,Y4]:')
plt.figure()
plt.plot(X4,Y4,'bo',label='datos')
plt.plot(X,np.polyval(coef14,X),label='poly3')
plt.plot(X,np.exp(np.polyval(coef24,X)),label='exp')
plt.plot(X,np.exp(np.polyval(coef34,np.log(X))),label='potencial')
plt.plot(X,1./np.polyval(coef44,1./X),label='crecimiento')
plt.plot(X,funcionexp1(X,*coef_exp4),label='Exponencial CURVE_FIT')
plt.plot(X,funcionpot1(X,*coef_pot4),label='Potencial CURVE_FIT')
plt.plot(X,funlogis(X,*coef_logis4),label='Logística')

plt.grid()
plt.legend()
plt.show()
