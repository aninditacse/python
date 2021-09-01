# -*- coding: utf-8 -*-
"""
Created on Sat Mar 13 16:28:39 2021

@author: Anindita
"""

A = dict() 
B = dict() 
Y = dict()

A={"a":0.2,"b":0.3,"c":0.6,"d":0.6}
#B={"a":0.9,"b":0.9,"c":0.4,"d":0.5}

for x in (A):
  t1=A[x]
  Y[x]=1-t1

print('Complement of set A is:',Y)