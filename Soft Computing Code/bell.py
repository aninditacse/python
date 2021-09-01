# -*- coding: utf-8 -*-
"""
Created on Thu Mar 25 09:19:29 2021

@author: Anindita
"""

import matplotlib.pyplot as plt
import numpy as np
import math

c=np.zeros((120), np.float)
c1=np.zeros((120), np.float)

mu=-1
sig=1
x_values=np.linspace(-3, 3, 120)
c[0:120]=x_values[0:120]
for  x in range (120):
  c1[x]=(1/(1+(abs((c[x] - mu)/sig)**(2*sig))))


plt.plot(c,c1)
plt.show()