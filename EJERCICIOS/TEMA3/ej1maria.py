# -*- coding: utf-8 -*-
"""
Created on Mon Sep 30 12:52:39 2019

@author: UO263483
"""


import numpy as N 
import numpy.linalg as LA


def norma(item, tipo):
    if item.ndim() ==1:
        if tipo==1:
            return N.sum(abs(item))
        if tipo==2:
            return N.sqrt(N.sum(item**2)) #comprobada que bien
        if tipo=='inf':
            return N.max(abs(item))
        else: 
         if tipo==1:
              item=N.abs(item)
              return N.max(N.sum(abs(item), axis=0)) #Axis 0-> columnas
         if tipo==2:
            auto=LA.eig(item)
            ro= N.max(auto[0])
            return N.sqrt(N.dot(item, item.T)*ro)
         if tipo== inf:
            return N.max(N.sum(abs(item), axis=1)

A=N.random.randint(10,size=(3,4))

print(norma(A,1))