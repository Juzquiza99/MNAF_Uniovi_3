import numpy as np
import matplotlib.pyplot as plt
import scipy.spatial as spatial
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
nparticulas = 100
l=15 
npasos=2000
dt=0.01
pausa=0.01
pasos=10
intervalo_choques=20
distchoque = 0.25
kb = 0.01
m=np.zeros(nparticulas)
m1=1 
m2=40
m[0:int(nparticulas/2)]=m1
m[int(nparticulas/2):]=m2
T = np.zeros(nparticulas)
T1=100
T[0:int(nparticulas/2)]=T1
energia0 = np.random.exponential(kb*T,(1,nparticulas))
v0 = (2*energia0/m)**0.5
fig=plt.figure(figsize=(6,6))
ax=fig.add_subplot(111) #Eje x
ax.set_xlim((0,l)) #Límites ejes
ax.set_ylim((0,l))
x=l*np.random.rand(nparticulas,2)
point1,=ax.plot(x[:50,0],x[:50,1],'ro') 
point2,=ax.plot(x[50:,0],x[50:,1],'bo')
angu0=2*np.pi*(np.random.rand(nparticulas))
v=v0.T*np.array([np.cos(angu0), np.sin(angu0)]).T
pasospresion=50

 

 

 


def choque(x1,x2,v1,v2,m1,m2):    
    distancia = (((x1-x2)[0])**2 + ((x1-x2)[1])**2)**0.5
    normal = (x2-x1)/distancia
    tangencial = np.array([-normal[1],normal[0]])
    if np.dot(v1,normal)-np.dot(v2,normal)>=0:
        v1normal = np.dot(v1,normal)
        v2normal = np.dot(v2,normal)
        v1normal,v2normal= (v2normal*m2+v1normal*(m1-m2))/(m1+m2),(2*v1normal*m1+v2normal*(m2-m1))/(m1+m2)  # aqui hay que poner una definicion mas general por si hay particulas de diferente masa,f(x1,x2,v1,v2,m1,m2)
        v1tangencial = np.dot(v1,tangencial)
        v2tangencial = np.dot(v2,tangencial)
        v1 = normal*v1normal + tangencial*v1tangencial
        v2 = normal*v2normal + tangencial*v2tangencial
    return v1,v2

 

 

 

 

 

energias = np.zeros(nparticulas)
presiontotal = np.zeros(npasos)
presion=np.zeros(int(npasos/pasospresion)) #queremos la presion cada x pasos

 

 

 

for i in range(npasos):
    x=x+dt*v
    presiontotal[i]=0
    for j in range(nparticulas):
        if x[j,0] <=0 :
            if v[j,0]<0:
                v[j,0]=-v[j,0]
                presiontotal[i]+=0.5*m[j]*np.abs(v[j,0])/l/dt
        if  x[j,0]>=l:
            if v[j,0]>0:
                v[j,0]=-v[j,0]
                presiontotal[i]+=0.5*m[j]*np.abs(v[j,0])/l/dt
        if x[j,1] <=0 :
            if v[j,1]<0:
                v[j,1]=-v[j,1]
                presiontotal[i]+=0.5*m[j]*np.abs(v[j,1])/l/dt
        if x[j,1]>=l:
            if v[j,1]>0:
                v[j,1]=-v[j,1]
                presiontotal[i]+=0.5*m[j]*np.abs(v[j,1])/l/dt    
        energias[j]=0.5*m[j]*(v[j,0]**2+v[j,1]**2)
    if np.mod(i,pasospresion)==(pasospresion-1):
                presion[int(i/pasospresion)]=np.mean(presiontotal[i-pasospresion:i])
    points_tree = spatial.cKDTree(x)
    pairs = points_tree.query_pairs(distchoque)
    for ipair in pairs:
        v[ipair[0],:],v[ipair[1],:]=choque(x[ipair[0],:],x[ipair[1],:],v[ipair[0],:],v[ipair[1],:],m[ipair[0]],m[ipair[1]])
    if i % pasos ==0:
        point1.set_data(x[:50,0],x[:50,1])
        point2.set_data(x[50:,0],x[50:,1]) 
        plt.pause(pausa)

 

 

 

'''
igual en la pregunta 2 del informe es mejor seguir definiendo un unico x 
donde la 1ª mitad del array son de la particula1 y la 2ª mitad las de la particula2
y un array de masas de dimension igual que x con la 1ª mitad m1 y la 2ª m2 para poder
referirnos a ellas como m[ipair[0],:]
'''

 

 

 

mediaenergias = np.mean(energias)
print(mediaenergias)

 

 

 

presion[0]=0
mediapresion = np.mean(presion)
print(mediapresion)

 

 

 

arraypresion=np.linspace(0,npasos,int(npasos/pasospresion))    
fig2,ax2 = plt.subplots()
ax2.hist(energias,bins = 25,range=(0,2*mediaenergias))
plt.figure()
plt.plot(arraypresion,presion)
plt.show()

 

 

 

'''
areadiscos = np.pi*distchoque**2
areareal = lado**2 - areadiscos

 

 

 

gideal=presionmedia*lado**2/nparticulas/kb/Tf
gwalls = presionmedia*areareal/nparticulas/kb/Tf
'''


 

 

'''
igual en la pregunta 2 del informe es mejor seguir definiendo un unico x 
donde la 1ª mitad del array son de la particula1 y la 2ª mitad las de la particula2
y un array de masas de dimension igual que x con la 1ª mitad m1 y la 2ª m2 para poder
referirnos a ellas como m[ipair[0],:]
'''

 

 

 

mediaenergias = np.mean(energias)
print(mediaenergias)

 

 

 

presion[0]=0
mediapresion = np.mean(presion)
print(mediapresion)

 

 

 

arraypresion=np.linspace(0,npasos,int(npasos/pasospresion))    
fig2,ax2 = plt.subplots()
ax2.hist(energias,bins = 25,range=(0,2*mediaenergias))
plt.figure()
plt.plot(arraypresion,presion)
plt.show()

 

 

 

'''
areadiscos = np.pi*distchoque**2
areareal = lado**2 - areadiscos

 

 

 

gideal=presionmedia*lado**2/nparticulas/kb/Tf
gwalls = presionmedia*areareal/nparticulas/kb/Tf
'''