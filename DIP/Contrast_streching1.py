# -*- coding: utf-8 -*-
"""
Created on Sun Mar  7 16:29:41 2021

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


norm_img2 = cv2.normalize(img, None, alpha=0, beta=1.2, norm_type=cv2.NORM_MINMAX, dtype=cv2.CV_32F)


norm_img2 = np.clip(norm_img2, 0, 1)
norm_img2 = (255*norm_img2).astype(np.uint8)


# display input and both output images
cv2.imshow('original',img)
#cv2.imshow('normalized1',norm_img1)
cv2.imshow('normalized2',norm_img2)
cv2.waitKey(0)
cv2.destroyAllWindows()