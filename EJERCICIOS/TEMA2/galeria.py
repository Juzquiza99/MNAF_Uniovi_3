# -*- coding: utf-8 -*-
"""
Created on Wed Oct 16 21:31:25 2019

@author: javie
"""

import numpy as np
import scipy.optimize as so
A1, A2, E, a = (5, 3, 0.2, 2*N.pi/3)
fn = lambda b: -(A1-E*np.cos(b))*np.cos(b)/np.sin(b)**2 - (A2+E*np.cos(a+b))*np.cos(a+b)/np.sin(a+b)**2
s, sdat = so.brentq(fn, 0.1,np.pi/3-0.1, full_output=True)
print(s,sdat)