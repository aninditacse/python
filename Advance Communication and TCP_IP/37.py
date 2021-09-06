# -*- coding: utf-8 -*-
"""
Created on Mon Jun 28 17:00:04 2021

@author: Anindita
"""

res=[]

test_str = "ani"
  
print("The original string is : " + str(test_str))
  
res = ''.join(format(ord(i), '08b') for i in test_str)
  
print("The string after binary conversion : " + str(res))

sub=[]
sub2=[]

k=len(res)
for i in range(2,k):
    if i>1:
        for j in range(2,i):
            if i%j==0:
                sub2.append(i)
                
                break
            else:
                sub.append(i)
print(sub2)

        
