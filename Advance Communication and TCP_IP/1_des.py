# -*- coding: utf-8 -*-
"""
Created on Tue Aug 10 10:30:44 2021

@author: Anindita
"""

inp=input("Enter the string: ")
while(len(inp)!=8):
 print('please enter 8 character string.')
 inp=input()
k=''.join(format(ord(i), '08b') for i in inp)
arr1=[]
n=len(k)
for i in range(n):
 if((i+1)%8!=0):
     arr1.append(k[i])
 
print(arr1) 
print("Length of string after discarding:",len(arr1))