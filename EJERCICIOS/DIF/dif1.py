# -*- coding: utf-8 -*-
"""
Created on Sat Nov 30 10:59:39 2019

@author: javie
"""
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 11 12:27:52 2019


@author: UO264982
"""
import matplotlib.pyplot as plt
import sympy as S


S.init_printing(use_unicode=True)
x,y,z = S.symbols('x y z',real=True)
funcion = (x+y)**z
a = S.diff(funcion,z,3)
b = funcion.diff(x,1,y,2)
c = S.Derivative(funcion,z,3)
c.doit()


import numpy as N
import scipy.misc as SM

#Número de puntos ha de ser impar
x = S.symbols('x',real=True)
funsym = S.exp(-x**2)
funnum = S.lambdify(x,funsym,"numpy")
z= 2
solsym = funsym.diff(x,1).subs(x,z).evalf()
solnum = SM.derivative(funnum,z, dx=1e-6)
pesos = SM.central_diff_weights(3)
print(solnum,pesos)



xs = S.symbols('x',real=True)
fsym = S.exp(-xs**2)
fnum = S.lambdify(xs,fsym,"numpy")
x = N.arange(-1,1,1/4)
y = fnum(x)
derfsym = fsym.diff(xs,1)
solsym = list([derfsym.subs(xs,z)for z in x])
s0 = N.array(solsym).astype(float)
s1 = N.diff(y)/N.diff(x)
s2 = N.gradient(y,x)
s3 = N.gradient(y,x,edge_order=2)




#EJEMPLO 4
#SOPORTE: 11 puntos equiespaciados en el intervalo [0,1]
import matplotlib.pyplot as plt
import sympy as S
import numpy as N
import scipy.misc as SM


xs = S.symbols('x',real=True)
fsym1=S.sin(xs)
fsym2=S.sqrt((1+xs))
n=11#número de puntos
sop=N.linspace(0,1,n)
fnum1=S.lambdify(xs,fsym1,'numpy')
y1=fnum1(sop)
fnum2=S.lambdify(xs,fsym2,'numpy')
y2=fnum2(sop)
error1=N.zeros_like(sop)
error2=N.zeros_like(sop)
derfsym1 = fsym1.diff(xs,1)
derfsym2 = fsym2.diff(xs,1)
solsym1 = list([derfsym1.subs(xs,z)for z in sop])
solsym2 = list([derfsym2.subs(xs,z)for z in sop])
s01 = N.array(solsym1).astype(float)
s02 = N.array(solsym2).astype(float)
s11 = N.diff(y1)/N.diff(sop)
s12 = N.diff(y2)/N.diff(sop)


funi1=N.cos(sop)
funi2=1./2*(1+(sop))**(-0.5)


def error1(f,x,aprox):
        error=N.zeros(len(x))
        y=f(x)
        for i in range(len(x)):
            error[i]=abs(y[i]-aprox[i])
        return error


print('Resultado ejemplo 4:')
plt.figure(1)
plt.plot(sop,s01,label='aprox. cos(x)')
plt.plot(sop[:-1],s11,label='aprox. cos(x)')
plt.plot(sop,N.cos(sop),label='cos(x)')
plt.plot(sop,s02,label='aprox.(1+x)^1/2')
plt.plot(sop[:-1],s12,label='aprox. (1+x)^1/2')
plt.plot(sop,1./2*(1+(sop))**(-0.5),label='d/dx((1+x)^1/2)')
plt.grid()
plt.legend()
plt.show()
print('Errores obtenidos:')
print(error1(lambda x: N.cos(x),sop[:-1],s11))
plt.figure(2)
plt.plot(sop[:-1],error1(lambda x: N.cos(x),sop[:-1],s11),'ro',label='Error dif(sin(x))')
plt.plot(sop[:-1],error1(lambda x: 1./2*(1+(x))**(-0.5),sop[:-1],s12),'bo',label='Error dif(1+x)**0.5')
plt.legend()
plt.grid()
plt.show()


#EJEMPLO 6
#formula es un vector de dos puntos donde indicamos el número de puntos donde se calcula la derivada
#y el segundo dónde se calcula la derivada


def calcdif(f,x,h,formula):
        der=N.zeros(len(x))
        for i in range(len(x)):
            if formula[0]==2:
                if formula[1]==0:
                    der[i]=(1./h)*(-f(x[i])+f(x[i]+h))
                elif formula[1]==1:
                    der[i]=(-1./h)*(-f(x[i])+f(x[i]-h))
                    
            elif formula[0]==3:
                if formula[1]==0:
                    der[i]=(1./h)*(-f(x[i])+f(x[i]+h))+(1./2*h)*(-3*f(x[i])+4*f(x[i]+h)-f(x[i]+2*h))
                elif formula[1]==1:
                    der[i]=(1./h)*(-f(x[i])+f(x[i]+h))+(1./2*h)*(-f(x[i])+f(x[i]+2*h))
                elif formula[1]==2:
                    der[i]=(1./h)*(-f(x[i])+f(x[i]+h))+(1./2*h)*(-3*f(x[i])+4*f(x[i]+h)-f(x[i]+2*h))+(1./2*h)*(-f(x[i])+f(x[i]+2*h))
            
            
        return der


n=11#número de puntos
sop=N.linspace(0,1,n)
fun1=lambda x:N.sqrt(1+x)
dfun1=lambda x:1./(2*N.sqrt(x+1))
print('Resultado ejemplo 6:')


a20=calcdif(fun1,sop,0.1,[2,0])   
a21=calcdif(fun1,sop,0.1,[2,1])
a30=calcdif(fun1,sop,0.1,[3,0])
a31=calcdif(fun1,sop,0.1,[3,1])
a32=calcdif(fun1,sop,0.1,[3,2])


def error2(f,x,aprox):
        error=N.zeros(len(x))
        y=f(x)
        for i in range(len(x)):
            error[i]=(y[i]-aprox[i])
        return error


print('Error:')
print(error2(dfun1,sop,a20))


plt.figure(3)
plt.plot(sop,a20,label='aprox. 2ptos-0')
plt.plot(sop,a21,label='aprox. 2ptos-1')
plt.plot(sop,a30,label='aprox. 3ptos-0')
plt.plot(sop,a31,label='aprox. 3ptos-1')
plt.plot(sop,a32,label='aprox. 3ptos-2')
plt.plot(sop,1./(2*N.sqrt(sop+1)),label='1/2(x+1)**0.5')
plt.grid()
plt.legend()
plt.show()


plt.figure(4)
plt.plot(sop,error2(dfun1,sop,a20),label='error aprox. 2ptos-0')
plt.plot(sop,error2(dfun1,sop,a21),label='error aprox. 2ptos-1')
plt.plot(sop,error2(dfun1,sop,a30),label='error aprox. 3ptos-0')
plt.plot(sop,error2(dfun1,sop,a31),label='error aprox. 3ptos-1')
plt.plot(sop,error2(dfun1,sop,a32),label='error aprox. 3ptos-2')
plt.legend()
plt.grid()
plt.show()
