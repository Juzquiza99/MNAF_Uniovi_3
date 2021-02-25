# -*- coding: utf-8 -*-
"""
Created on Wed Oct 16 19:07:09 2019

@author: javier
"""
import numpy as N
import time as T
import sympy as S

x = S.Symbol('x')
y, z = S.symbols('y z')
f = x**3-2*x+S.sin(x)
k = f.subs(x,1)
fn = S.lambdify(x,f,"numpy")
fs = fn(x)
X = N.random.rand(1000)
tinic = T.time()
for y in X: f.subs(x,y)
print("Simbolico (s): {}".format(T.time()-tinic))
tinic = T.time()
for y in X: fn(y)
print("Numerico (s): {}".format(T.time()-tinic))