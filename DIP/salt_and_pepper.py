# -*- coding: utf-8 -*-
"""
Created on Sun Mar  7 21:12:17 2021

@author: Anindita
"""

import random 
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

def add_noise(img): 
  
   
    row , col = img.shape 
      
    number_of_pixels = random.randint(300, 10000) 
    for i in range(number_of_pixels): 
        
         
        y_coord=random.randint(0, row - 1) 
          
        x_coord=random.randint(0, col - 1) 
          
        img[y_coord][x_coord] = 255
          
    
    number_of_pixels = random.randint(300 , 10000) 
    for i in range(number_of_pixels): 
        
        y_coord=random.randint(0, row - 1) 
          
        x_coord=random.randint(0, col - 1) 
          
        img[y_coord][x_coord] = 0
          
    return img 
  
cv2.imshow('input image',img)
cv2.waitKey(0)    
cv2.imshow('output image',add_noise(img))
cv2.waitKey(0)
cv2.destroyAllWindows()