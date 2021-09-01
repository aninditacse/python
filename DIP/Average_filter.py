# -*- coding: utf-8 -*-
"""
Created on Sun Mar  7 20:23:09 2021

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


img=readfile(r'C:\Users\Anindita\Desktop\Python Lab\original1.pgm') 
  
m, n = img.shape 
   
mask = np.ones([3, 3], dtype = int) 
mask = mask / 9
     
img_new = np.zeros([m, n]) 
  
for i in range(1, m-1): 
    for j in range(1, n-1): 
        temp = img[i-1, j-1]*mask[0, 0]+img[i-1, j]*mask[0, 1]+img[i-1, j + 1]*mask[0, 2]+img[i, j-1]*mask[1, 0]+ img[i, j]*mask[1, 1]+img[i, j + 1]*mask[1, 2]+img[i + 1, j-1]*mask[2, 0]+img[i + 1, j]*mask[2, 1]+img[i + 1, j + 1]*mask[2, 2] 
         
        img_new[i, j]= temp 
          
img_new = img_new.astype(np.uint8)
cv2.imshow('input image',img)
cv2.waitKey(0)

cv2.imshow('output image',img_new)
cv2.waitKey(0)
cv2.destroyAllWindows()
 