# -*- coding: utf-8 -*-
"""
Created on Sat Mar 20 13:51:09 2021

@author: Anindita
"""

import numpy as np
import cv2
#from matplotlib import pyplot as plt

def readfile(image):
    img1=open(image,"r")
    p1=img1.readline()
    p2=img1.readline()
    t1=img1.readline()
    p3=img1.readline()
    width,height=[int(i) for i in t1.split()]
    imag=np.zeros((height,width), dtype=np.uint8)
    for i in range(height):
        for j in range(width):
            imag[i,j]=img1.readline()
            
    return(imag,p1,p2,t1,p3)
    

def writefile(img,t1,t2,t3,t4):
    im=open(r'C:\Users\Anindita\Desktop\Python Lab\original1_lapla3.pgm',"w")
    im.write("%s"%t1)
    im.write("%s"%t2)
    im.write("%s"%t3)
    im.write("%s"%t4)
    h=img.shape[0]
    w=img.shape[1]
    
    for i in range(h):
        for j in range(w):
            im.write("%d\n"%img[i,j])

    im.close()

img,p1,p2,t1,p3=readfile(r'C:\Users\Anindita\Desktop\Python Lab\original3.pgm')

dimension=img.shape
print(dimension)
height=img.shape[0]
width=img.shape[1]
mask=np.zeros((3,3), dtype=np.uint8)

mask=np.array([[1,2,1],
      [2,4,2],
      [1,2,1]])
mask1=np.array([[0,1,0],
      [1,-4,1],
      [0,1,0]])

imag=np.zeros((height,width), dtype=np.uint8)
imag1=np.zeros((height,width), dtype=np.uint8)

for i in range(2,height-1,1):
    for j in range(2,width-1,1):
        imag[i,j]=(img[i-1, j-1]*mask1[0, 0]+img[i-1, j]*mask1[0, 1]+img[i-1, j + 1]*mask1[0, 2]+img[i, j-1]*mask1[1, 0]+ img[i, j]*mask1[1, 1]+img[i, j + 1]*mask1[1, 2]+img[i + 1, j-1]*mask1[2, 0]+img[i + 1, j]*mask1[2, 1]+img[i + 1, j + 1]*mask1[2, 2])


imag1=writefile(imag,p1,p2,t1,p3)
print(imag)
cv2.imshow('image',imag)
cv2.waitKey(0)
cv2.destroyAllWindows()