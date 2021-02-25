#coding:utf-8
from numpy import *
import numpy.linalg as nl
import numpy.random as rnd
import scipy.optimize as so

def Doolittle(A):
	L=zeros_like(A)+identity(shape(A)[0])
	U=zeros_like(A)
	U[0,0]=A[0,0]
	for i in range(shape(A)[0]):
		for j in range(shape(A)[1]):
			if j>=i:
				s=0
				for k in range(i):
					s+=L[i][k]*U[k][j]
				U[i][j]=A[i][j]-s
			if j<i:
				s=0
				for k in range(j):
					s+=L[i][k]*U[k][j]
				L[i][j]=1./U[j][j]*(A[i][j]-s)
	print(L,U)
	return dot(L,U) #A=L*U


A=rnd.randint(10,size=(3,3))
A=A.astype('float')

def Crout(A):
	L=zeros_like(A)+identity(shape(A)[0])
	D=zeros_like(A)
	D[0,0]=A[0,0]
	for i in range(shape(A)[0]):
		for j in range(shape(A)[0]):
			if i==j:
				s=0
				for k in range(i-1):
					s+=L[i,k]*D[i,i]*L[i,k]
				D[i,j]=A[i,i]-s
			elif j<i:
				s=0
				for k in range(i-1):
					s+=L[i,k]*D[i,i]*L[j,k]
				L[i,j]=1./D[j,j]*(A[i,j]-s)
	N=dot(L,D)
	M=dot(N,L.T)
	return L, L.T, M

A=A+A.T

def Cholesky(A):
	A=A.astype('complex')
	L=zeros_like(A)
	L[0][0]=sqrt(A[0][0])
	for i in range(shape(A)[0]):
		for j in range(shape(A)[0]):
			if i==j:
				s=0
				for k in range(i):
					s+=L[i,k]*L[i,k]
				L[i,i]=sqrt(A[i,j]-s)
			if i>j:
				s=0
				for k in range(i):
					s+=L[i,k]*L[j,k]
				L[i,j]=1./L[j,j]*(A[i,j]-s)
	return L#,L.T, dot(L,L.T)
print(A)
#print(Cholesky(A))#print(Cholesky(A).astype(float))
B=array([[6,3,4,8],[3,6,5,1],[4,5,10,7],[8,1,7,25]])
print(Cholesky(B))
print(nl.cholesky(B))