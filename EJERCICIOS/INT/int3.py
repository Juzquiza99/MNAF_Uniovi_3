# -*- coding: utf-8 -*-
"""
Editor de Spyder

Este es un archivo temporal
"""

import sympy as S
import numpy as N
import scipy.integrate as sc

#EJERCICIO 11

#Tener en cuenta:
#formulas cerradas:n=-1:trapecio, n=-2:simpson
#formulas abiertas:n=0:punto medio, n=1:trapecio abierto
                #n=2:milne, n=3:wilms
                
#En las fórmulas cerradas utilizaremos los puntos del soporte como puntos donde calcular
#las imágnenes de las funciones según sean en cada caso las fórmulas.

def integracion(f,inter,orden,nint):
    a,b=inter[0],inter[1]
    sop=N.linspace(a,b,nint+1) #Creamos un soporte

    if orden==-1: #trapecio cerrado
        print('Con trapz:')
        y1=f(sop) #y's de la función
        for i in range(nint):
            sol_trap=sc.trapz(y1,sop)
        print(sol_trap)
        
        print('Con trapecio fórmula:') #Ahora lo calculamos con la fórmula cerrada
        h=(b-a)/(nint)
        sol_trapintcer=N.zeros(nint)
        
        for i in range(nint):
            sol_trapintcer[i]=0.5*h*(f(sop[i])+f(sop[i+1]))
        sol_trapcerrado=sum(sol_trapintcer)
        
        return(sol_trapcerrado)
        
    if orden==-2: #simpson
        print('Con simps:')
        y1=f(sop) #y's de la función
        sol_simps=sc.simps(y1,sop)
        print(sol_simps)
        
        print('Con Simpson fórmula:')
        h=(b-a)/(2*nint)
        sol_simpsintcer=N.zeros(nint)
        x1=N.zeros(nint)
        
        for i in range(nint):
            x1[i]=sop[i]+h
            sol_simpsintcer[i]=(1./3)*h*(f(sop[i])+4*f(x1[i])+f(sop[i+1]))
        sol_simpsfor=sum(sol_simpsintcer)
        return(sol_simpsfor)
        
    #De igual forma calcularíamos la regla de 3/8 de Simpson, dividiendo cada intervalo
    #en 3 subintervalos y calculando entonces x1 y x2, además de los a (x0 y b(x3)
    #Mismo proceder para la regla de Boole, con una división más.
        
    if orden==0: #punto medio
        x0=N.zeros(nint)
        h=(b-a)/(2*nint)
        sol_pmint=N.zeros(nint) #resultado de cada intervalo
        for i in range(nint):
            x0[i]=sop[i]+h
            sol_pmint[i]=2*h*f(x0[i]) #valor de cada subintervalor
        sol_pmedio=sum(sol_pmint)
        
        return(sol_pmedio)
        
    if orden==1: #trapecio abierto
        x0=N.zeros(nint)
        x1=N.zeros(nint)
        h=(b-a)/(3*nint)
        sol_trapint=N.zeros(nint)
        for i in range(nint):
            x0[i]=sop[i]+h
            x1[i]=sop[i]+2*h
            sol_trapint[i]=1.5*h*(f(x0[i])+f(x1[i]))
        sol_trapabierto=sum(sol_trapint)
        
        return(sol_trapabierto)
    
    if orden==2: #Regla de Milne
        x0=N.zeros(nint)
        x1=N.zeros(nint)
        x2=N.zeros(nint)
        h=(b-a)/(4*nint)
        sol_milneint=N.zeros(nint)
        for i in range(nint):
            x0[i]=sop[i]+h
            x1[i]=sop[i]+2*h
            x2[i]=sop[i]+3*h
            sol_milneint[i]=((4*h)/3)*(2*f(x0[i])-f(x1[i])+2*f(x2[i]))
        sol_milne=sum(sol_milneint)
        
        return(sol_milne)
        
    if orden==3: #Regla de Wilms
        x0=N.zeros(nint)
        x1=N.zeros(nint)
        x2=N.zeros(nint)
        x3=N.zeros(nint)
        h=(b-a)/(5*nint)
        sol_wilmsint=N.zeros(nint)
        for i in range(nint):
            x0[i]=sop[i]+h
            x1[i]=sop[i]+2*h
            x2[i]=sop[i]+3*h
            x3[i]=sop[i]+4*h
            sol_wilmsint[i]=((5*h)/24)*(11*f(x0[i])+f(x1[i])+f(x2[i])+11*f(x3[i]))
        sol_wilms=sum(sol_wilmsint)
        
        return(sol_wilms)
    
f1=lambda x: x**2
f2=lambda x: N.sin(x)
for i in range(-2,4):
    print(integracion(f2,[0,1],i,201))



#CUADRATURA
#EJEMPLO 12

f1=lambda x: N.sin(x)
f2=lambda x: 1/(1+x**2)
f3=lambda x: N.exp(-x**2)
f4=lambda x: N.sqrt(1+x**2)
int1,int2,int3,int4=(0,N.pi),(0,5),(0,4),(-1,1)

funciones=[f1,f2,f3,f4]
intervalos=[int1,int2,int3,int4]

for i in range(len(funciones)):
    solu=sc.fixed_quad(funciones[i],*intervalos[i])
    print(solu)


#INTEGRAL DOBLE
a,b=(0,1)
yinf=lambda x:x**2
ysup= lambda x:N.sqrt(x)
fun= lambda x, y: x**2 + y**3
sol=sc.dblquad(fun,a,b,yinf,ysup)
print(sol)

#Con sympy sería:
#sol=S.integrate(S.integrate(x**2+y**3,(y,x**2,S.sqrt(x))),(x,0,1))
#print(sol)
