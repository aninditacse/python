# -*- coding: utf-8 -*-
"""
Created on Sun Mar  7 19:34:25 2021

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
  
# Apply log transform. 
c = 255/(np.log(1 + np.max(img))) 
log_transformed = c * np.log(1 + img) 
  
# Specify the data type. 
log_transformed = np.array(log_transformed, dtype = np.uint8) 
  
cv2.imshow('input image',img)
cv2.waitKey(0)
cv2.imshow('output image',log_transformed)
cv2.waitKey(0)
cv2.destroyAllWindows()
