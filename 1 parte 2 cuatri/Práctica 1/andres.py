import numpy as np
import matplotlib.pyplot as plt
import scipy.spatial as spatial
from scipy.optimize import curve_fit

 

'''
Datos del problema:
lado caja: 10
masa disco 1
ci:
posicion inicial (x0) aleatoria
vo=1, direccion aleatoria
dt=0.01
num pasos:10000
pasos entre reps:10
pausa entre repres:0.01s
'''
m=1 #masa disco
distchoque = 0.25
areadiscos = np.pi*distchoque**2
areainversa=np.linspace (1/(100-areadiscos),1/(1500-areadiscos),20)
area=1/areainversa
l=np.sqrt(area)
repreP=np.zeros(len(l))
npasos=1000
dt=0.01
pausa=0.01
pasos=10
nparticulas = 150
intervalo_choques=20
kb = 0.01
T = 25
energia0 = np.random.exponential(kb*T,(1,nparticulas))
v0 = (2*energia0/m)**0.5

 

pasospresion=50

 


def choque(x1,x2,v1,v2):    
    distancia = (((x1-x2)[0])**2 + ((x1-x2)[1])**2)**0.5
    normal = (x2-x1)/distancia
    tangencial = np.array([-normal[1],normal[0]])
    if np.dot(v1,normal)-np.dot(v2,normal)>=0:
        v1normal = np.dot(v1,normal)
        v2normal = np.dot(v2,normal)
        v1normal,v2normal= v2normal,v1normal  # aqui hay que poner una definicion mas general por si hay particulas de diferente masa,f(x1,x2,v1,v2,m1,m2)
        v1tangencial = np.dot(v1,tangencial)
        v2tangencial = np.dot(v2,tangencial)
        v1 = normal*v1normal + tangencial*v1tangencial
        v2 = normal*v2normal + tangencial*v2tangencial
    return v1,v2

 

 

energias = np.zeros(nparticulas)
presiontotal = np.zeros(npasos)
presion=np.zeros(int(npasos/pasospresion)) #queremos la presion cada x pasos

 

for k in range(len(l)):
    #fig=plt.figure(figsize=(6,6))
    #ax=fig.add_subplot(111) #Eje x
    #ax.set_xlim((0,l[k])) #Límites ejes
    #ax.set_ylim((0,l[k]))
    x=l[k]*np.random.rand(nparticulas,2)
    #point,=ax.plot(x[0],x[1],'ro') 
    angu0=2*np.pi*(np.random.rand(nparticulas))
    v=v0.T*np.array([np.cos(angu0), np.sin(angu0)]).T
    for i in range(npasos):
        x=x+dt*v
        presiontotal[i]=0
        for j in range(nparticulas):
            if x[j,0] <=0 :
                if v[j,0]<0:
                    v[j,0]=-v[j,0]
                    presiontotal[i]+=0.5*m*np.abs(v[j,0])/l[k]/dt
            if  x[j,0]>=l[k]:
                if v[j,0]>0:
                    v[j,0]=-v[j,0]
                    presiontotal[i]+=0.5*m*np.abs(v[j,0])/l[k]/dt
            if x[j,1] <=0 :
                if v[j,1]<0:
                    v[j,1]=-v[j,1]
                    presiontotal[i]+=0.5*m*np.abs(v[j,1])/l[k]/dt
            if x[j,1]>=l[k]:
                if v[j,1]>0:
                    v[j,1]=-v[j,1]
                    presiontotal[i]+=0.5*m*np.abs(v[j,1])/l[k]/dt    
            energias[j]=0.5*m*(v[j,0]**2+v[j,1]**2)
        if np.mod(i,pasospresion)==(pasospresion-1):
                    presion[int(i/pasospresion)]=np.mean(presiontotal[i-pasospresion:i])
        points_tree = spatial.cKDTree(x)
        pairs = points_tree.query_pairs(distchoque)
       
        for ipair in pairs:
            v[ipair[0],:],v[ipair[1],:]=choque(x[ipair[0],:],x[ipair[1],:],v[ipair[0],:],v[ipair[1],:])
        #if i % pasos ==0:
            #point.set_data(x[:,0],x[:,1]) 
            #plt.pause(pausa)
    
    mediaenergias = np.mean(energias)
    presion[0]=0
    mediapresion = np.mean(presion)
    repreP[k]=mediapresion

 

def f(x,m,b):
    return m*x+b 

 

areainversa=areainversa
popt,pcov = curve_fit(f,areainversa,repreP)
print(popt[0])
X=np.linspace(0.01,0.00067,500)
plt.plot(areainversa,repreP,'bx')
plt.plot(X,popt[0]*X+popt[1],label='ajuste')
plt.xlabel('$A^{-1}$')
plt.ylabel('P')
plt.title('P vs $A^{-1}$')
plt.legend()
plt.show()      