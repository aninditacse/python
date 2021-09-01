# -*- coding: utf-8 -*-
"""
Created on Sat Mar 13 16:31:08 2021

@author: Anindita
"""

import matplotlib.pyplot as plt
import numpy as np
a=int (input('Enter first value: '))
b=int (input('Enter second value: '))
m=(a+b)/2
c=np.zeros((40),np.int)
c1=np.zeros((40),np.float)

for x in range (40):
  c[x]=x
  if x<a:
    y=0
    c1[x]=y
  if a<=x<m:
    y=(x-a)/(m-a)
    c1[x]=y
  if m<=x<=b:
    y=(b-x)/(b-m)
    c1[x]=y
  if x>b:
    y=0
    c1[x]=y
plt.plot(c,c1)
plt.show()
