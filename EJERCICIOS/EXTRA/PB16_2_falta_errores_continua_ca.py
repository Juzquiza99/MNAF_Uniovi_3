# -*- coding: utf-8 -*-
"""
Created on Wed Nov  6 14:39:17 2019

@author: alumno
"""


import matplotlib.pyplot as plt
import numpy as np
import scipy.integrate as SI


print("\n")
print('APROXIMACIÓN CONTINUA CON ERROR')
print("\n")
'''
Base=[lambda x: np.ones_like(x)]
Base.append(lambda x: 1/x)
Base.append(lambda x: np.sqrt(x))
'''

a=lambda x: np.ones_like(x)
b=lambda x: 1/x
c=lambda x: np.sqrt(x)

d= lambda x: x
e= lambda x: x**2

f= lambda x: np.sin(x)
g= lambda x: np.cos(x)




Base1=np.array([a,b,c])
Base2=np.array([a,d,e])
Base3=np.array([a,f,g])




funcion=lambda x: 1/(1+x**2)
a,b=[1,5]
#print(Base)

def aproximacion_continua(Base,a,b,funcion):
    #resolver el sisstema Gc=f
    
    #funcion es la función que queremos aproximar
    #n=3 #orden de la base
    n=len(Base) #orden de la base
    G=np.zeros((n,n))
    arrayf=np.zeros(n)
    for i in range(n):
        for j in range(i,n):
            #HAY QUE ESPECIFICAR EN EL PRODUCTO QUE DEPENDEN DE X (x)
            producto1= lambda x: Base[i](x)*Base[j](x)
            G[i,j],error1=SI.quad(producto1,a,b)
            G[j,i]=G[i,j]
        #HAY QUE ESPECIFICAR EN EL PRODUCTO QUE DEPENDEN DE X (x)    
        producto2= lambda x: Base[i](x)*funcion(x)
        arrayf[i],error2=SI.quad(producto2,a,b)
    #resolvemos el sistema aproximado
    coefsc=np.linalg.solve(G,arrayf)
    '''
    #CÁLCULO DE ERRORES
    primero=np.dot(Y2,Y2)
    segundo=np.dot(coefsc,arrayf)
    tercero=np.sum(np.outer(coefsc.T,coefsc)*G)
    EC=primero-2*segundo+tercero
    ECM=EC*(1/(abs(b-a)))
    S=np.sqrt((EC*len(coefsc))/(abs(b-a)))
    '''    
    return coefsc
    #, EC, ECM, S


#Las pruebas nos devuelven los coeficientes de la aprximación en cada caso, que
#son la solucion de Gc=f    
print('Base 1')
coefsc1=aproximacion_continua(Base1,a,b,funcion) 
#, ECc1, ECMc1, Sc1
print(coefsc1)
'''
print('EC1:' +str(ECc1))
print("\n")
print('ECM1:' +str(ECMc1))
print("\n" )
print('S1:' +str(Sc1))
print("\n" )
'''

#LOS COEFICIENTES DE LA CONTINUA DAN BIEN (estaba bien de antes) PERO FALLA EL ERROR
print('Base 2')
coefsc2=aproximacion_continua(Base2,a,b,funcion) 
print(coefsc2) 

print('Base 3')
coefsc3=aproximacion_continua(Base3,a,b,funcion) 
print(coefsc3)  


#Lo representamos en cada caso
#la solución aproximada es el resultados de multiplicar cada elemento de coefs por 
#el elemento de l base que le corresponde:
#c0*base0+c1*base1+c2*base por ejemplo

puntos_representacion=201
X=np.linspace(a,b,puntos_representacion)
Y=funcion(X)
Z=np.zeros((3,puntos_representacion), dtype=float)
for i in range(coefsc1.size):
    Z[0]+= coefsc1[i]*Base1[i](X)
    Z[1]+= coefsc2[i]*Base2[i](X)
    Z[2]+= coefsc3[i]*Base3[i](X)

fig=plt.figure(1,figsize=(8,6))
plt.subplot(2,1,1)
plt.title('Función vs aproximaciones')
plt.plot(X,Z[0], label='Base 1')
plt.plot(X,Z[1], label='Base 2')
plt.plot(X,Z[2], label='Base 3')

plt.plot(X,Y, label='Función original')
plt.grid()
plt.legend()
plt.show()


print("\n")
print('_____________________________________________________________________')
print("\n")
print('APROXIMACIÓN DISCRETA CON ERROR')
print("\n")


X2=np.linspace(1,5,5) #soporte
Y2=funcion(X2)


def aproximacion_discreta(Base,X2,Y2):
    #resolver el sistema Ax=b
    
    n=len(Base) #número de funciones de la base
    m=len(X2)
    x=np.zeros((n,m))
    for i in range(n):
        #De esta manera estamos calculando directamente la xt
        #Base[i](X2) nos devuelve la funcion i en cada punto de X2 
        x[i]=Base[i](X2)
    G=np.dot(x,x.T)
    arrayf=np.dot(x,Y2)
    coefsd=np.linalg.solve(G,arrayf)
    
    #CÁLCULO DE ERRORES
    primero=np.dot(Y2,Y2)
    segundo=np.dot(coefsd,arrayf)
    tercero=np.sum(np.outer(coefsd.T,coefsd)*G)
    #tercero=np.multidot(coefsd.T,G,coefsd)
    EC=primero-2*segundo+tercero
    ECM=EC/len(X2)
    S=np.sqrt(EC/(len(X2)-len(coefsd)))
    
    
    
    '''
    #CÁLCULO DE ERRORES
    Phi=np.dot(coefsd,Base(x))
    error=Y2-Phi(X2)
    EC=np.dot(error,error)
    ECM=EC/len(X2)
    S=np.sqrt(EC/(len(X2)-len(coefsd)))
    come1=1-(EC/np.var(Y2)*(N-1)) #que es esta N?????
    '''
    return coefsd, EC, ECM, S


print('Base 1')
coefsd1, EC1, ECM1, S1 =aproximacion_discreta(Base1,X2,Y2) 
print(coefsd1)
print('EC1:' +str(EC1))
print("\n")
print('ECM1:' +str(ECM1))
print("\n" )
print('S1:' +str(S1))
print("\n" )



print('Base 2')
coefsd2, EC2, ECM2, S2 =aproximacion_discreta(Base2,X2,Y2) 
print(coefsd2) 
print('EC2:' +str(EC2))
print("\n")
print('ECM2:' +str(ECM2))
print("\n" )
print('S2:' +str(S2))
print("\n" )


print('Base 3')
coefsd3, EC3, ECM3, S3 =aproximacion_discreta(Base3,X2,Y2) 
print(coefsd3)
print('EC3:' +str(EC3))
print("\n")
print('ECM3:' +str(ECM3))
print("\n" )
print('S3:' +str(S3))
print("\n" )


puntos_representacionD=201
XD=np.linspace(a,b,puntos_representacionD)
YD=funcion(X)
ZD=np.zeros((3,puntos_representacionD), dtype=float)
for i in range(coefsd1.size):
    ZD[0]+= coefsd1[i]*Base1[i](X)
    ZD[1]+= coefsd2[i]*Base2[i](X)
    ZD[2]+= coefsd3[i]*Base3[i](X)

fig=plt.figure(1,figsize=(8,6))
plt.subplot(2,1,1)
plt.title('Función vs aproximaciones discretas')
plt.plot(XD,ZD[0], label='Base 1')
plt.plot(XD,ZD[1], label='Base 2')
plt.plot(XD,ZD[2], label='Base 3')

plt.plot(XD,YD, label='Función original')
plt.grid()
plt.legend()
plt.show()
