# -*- coding: utf-8 -*-
"""
Created on Wed Oct 16 19:28:00 2019

@author: javie
"""
import sympy as S
import numpy as np

from sympy.abc import x

f1=S.sin(x)+0.8*S.cos(x)
S.plot(f1,(x,5,6))
s1=S.solve(f1,x)

np.array(s1).astype(complex) #pasa a numérico
s1=S.solve(S.sin(x)+0.8*S.cos(x),x,dict=True)
f1.subs(s1[0]).evalf()
print(s1)


f2=x**2-4*x+3.5-S.log(x)
S.plot(f2,(x,1,3))
s2=S.solve(f2,x)
print(s2)
np.array(s2).astype(complex) # pasa a  numérico
s2=S.solve(f2,dict=True)
f2.subs(s2[0]).evalf()

f3=(x-2.1)**2 - 7*x*S.cos(x)
S.plot(f3,(x,1,2))
s3=S.solve(f3,x)
print(s3)
