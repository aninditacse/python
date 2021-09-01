# -*- coding: utf-8 -*-
"""
Created on Sun Mar  7 22:04:59 2021

@author: Anindita
"""

import cv2 
import numpy as np 
import matplotlib.pyplot as plt 
   
def hist_plot(img): 
      
    count =[]       
    r = [] 
    for k in range(0, 256): 
        r.append(k) 
        count1 = 0
        for i in range(m): 
            for j in range(n): 
                if img[i, j]== k: 
                    count1+= 1
        count.append(count1) 
          
    return (r, count) 
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
r1, count1 = hist_plot(img) 
   
plt.stem(r1, count1) 
plt.xlabel('intensity value') 
plt.ylabel('number of pixels') 
plt.title('Histogram of the original image') 
#plt.savefig('output.jpg')