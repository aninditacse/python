# -*- coding: utf-8 -*-
"""
Created on Sat Mar 13 16:24:14 2021

@author: Anindita
"""

A = dict() 
B = dict() 
Y = dict()

A={"a":0.2,"b":0.3,"c":0.6,"d":0.6}
B={"a":0.9,"b":0.9,"c":0.4,"d":0.5}

for x,y in zip(A,B):
  t1=A[x]
  t2=B[y]

  if t1>t2:
    Y[x]=t1
  else:
    Y[y]=t2

print('Union of two fuzzy sets A and B is:',Y)
