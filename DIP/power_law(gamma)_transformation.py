# -*- coding: utf-8 -*-
"""
Created on Sun Mar  7 19:49:49 2021

@author: Anindita
"""

import cv2 
import numpy as np 
  
def readfile(Image):
    img1=open(Image,"r")
    img1.readline()
    img1.readline()
    t1=img1.readline()
    img1.readline()
    width,height=[int(i) for i in t1.split()]
    imag=np.zeros((height,width), dtype=np.uint8)
    for i in range(height):
        for j in range(width):
            imag[i,j]=img1.readline()
    return(imag)


img=readfile(r'C:\Users\Anindita\Desktop\Python Lab\original.pgm') 
  
for gamma in [0.1, 0.5, 1.2, 2.2]: 
      
    # Apply gamma correction. 
    gamma_corrected = np.array(255*(img / 255) ** gamma, dtype = 'uint8')
    
    cv2.imshow('output image'+str(gamma),gamma_corrected)
    
    cv2.waitKey(0)
    cv2.destroyAllWindows()
  
    