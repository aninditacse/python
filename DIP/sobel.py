# -*- coding: utf-8 -*-
"""
Created on Tue Mar  9 19:19:12 2021

@author: Anindita
"""

import numpy as np
import cv2
from matplotlib import pyplot as plt
import math  

def readfile(image):
    img1=open(image,"r")
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

dimension=img.shape
print(dimension)
height=img.shape[0]
width=img.shape[1]
mask=np.zeros((3,3), dtype=np.uint8)

mask1=np.array([[-1,0,1],
      [-2,0,2],
      [-1,0,1]])

mask2=np.array([[-1,-2,-1],
      [0,0,0],
      [1,2,1]])

imag=np.zeros((height,width), dtype=np.uint8)


for i in range(0,height-1,1):
    for j in range(0,width-1,1):
        t1=(img[i-1, j-1]*mask1[0, 0]+img[i-1, j]*mask1[0, 1]+img[i-1, j + 1]*mask1[0, 2]+img[i, j-1]*mask1[1, 0]+ img[i, j]*mask1[1, 1]+img[i, j + 1]*mask1[1, 2]+img[i + 1, j-1]*mask1[2, 0]+img[i + 1, j]*mask1[2, 1]+img[i + 1, j + 1]*mask1[2, 2])
        t2=(img[i-1, j-1]*mask2[0, 0]+img[i-1, j]*mask2[0, 1]+img[i-1, j + 1]*mask2[0, 2]+img[i, j-1]*mask2[1, 0]+ img[i, j]*mask2[1, 1]+img[i, j + 1]*mask2[1, 2]+img[i + 1, j-1]*mask2[2, 0]+img[i + 1, j]*mask2[2, 1]+img[i + 1, j + 1]*mask2[2, 2])
        imag[i,j]=abs(math.sqrt((t1**2)+(t2**2)))



print(img)
print(imag)
cv2.imshow('input image',img)
cv2.waitKey(0)
cv2.imshow('output image',imag)
cv2.waitKey(0)
cv2.destroyAllWindows()