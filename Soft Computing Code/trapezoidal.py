# -*- coding: utf-8 -*-
"""
Created on Sat Mar 13 16:34:13 2021

@author: Anindita
"""

import matplotlib.pyplot as plt
import numpy as np
a=int (input('Enter first value: '))
b=int (input('Enter second value: '))
c=int (input('Enter third value: '))
d=int (input('Enter fourth value: '))

ci=np.zeros((60),np.int)
c1=np.zeros((60),np.float)

for x in range (60):
  ci[x]=x
  if x<a:
    y=0
    c1[x]=y
  if a<=x<=b:
    y=(x-a)/(b-a)
    c1[x]=y
  if b<=x<=c:
    y=1
    c1[x]=y
  if c<=x<d:
    y=(d-x)/(d-c)
    c1[x]=y
  if x>d:
    y=0
    c1[x]=y
    
plt.plot(ci,c1)
plt.show()
