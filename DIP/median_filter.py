# -*- coding: utf-8 -*-
"""
Created on Sun Mar  7 19:22:20 2021

@author: Anindita
"""

import cv2 
import numpy as np
from matplotlib import pyplot as plt 
  
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


img=readfile(r'C:\Users\Anindita\Desktop\Python Lab\original1.pgm')

m, n = img.shape 
   
img_new1 = np.zeros([m, n]) 
  
for i in range(1, m-1): 
    for j in range(1, n-1): 
        temp = [img[i-1, j-1], 
               img[i-1, j], 
               img[i-1, j + 1], 
               img[i, j-1], 
               img[i, j], 
               img[i, j + 1], 
               img[i + 1, j-1], 
               img[i + 1, j], 
               img[i + 1, j + 1]] 
          
        temp = sorted(temp) 
        img_new1[i, j]= temp[4] 
  
img_new1 = img_new1.astype(np.uint8) 
cv2.imshow('ouput',img_new1)
cv2.waitKey(0)
cv2.destroyAllWindows()

