#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 27 09:47:05 2020

@author: andrespresavilla
"""

 
import numpy as np
from matplotlib import pyplot as plt

n=100 #number of iterations +1
t0=0 #starting time
m0=20 #initial population
dt = 1 #time interval in seconds
a = 0.1 #rate constant
K = 2000 #carrying capacity
 
def growth(n,t0,m0,dt,a,K):
     malthus = np.zeros((n,2))
     malthus[0,0] = t0
     malthus[0,1] = m0
     for i in range(n-1):
         malthus[i+1,0] = malthus[i,0] + dt
         malthus[i+1,1] = a*malthus[i,1]*(1-malthus[i,1]/K)*dt + malthus[i,1]
         plt.plot(malthus[:,0],malthus[:,1],"ko") 
         plt.title("Malthus Growth")
         plt.xlabel("Seconds")
         plt.ylabel("Population")
         plt.show()
 
growth(n,t0,m0,dt,a,K) #run program