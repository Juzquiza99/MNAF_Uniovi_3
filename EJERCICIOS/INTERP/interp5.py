# -*- coding: utf-8 -*-
"""
Created on Mon Oct 28 13:44:25 2019

@author: UO264982
"""
#BIDIMENSIONAL

import numpy as N
import matplotlib.pyplot as plt
import scipy.interpolate as si 
from matplotlib import cm
from mpl_toolkits import mplot3d
superficie=lambda x,y: N.sin(N.sqrt(x**2+y**2))
npts=7
a,b=(-5,5)
x = N.linspace(a,b, npts)
y = N.linspace(a,b, npts)
xx, yy = N.meshgrid(x, y)
z = superficie(xx,yy)
p=si.interp2d(x,y,z,kind='linear')
