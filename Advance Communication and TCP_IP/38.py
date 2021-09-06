# -*- coding: utf-8 -*-
"""
Created on Mon Jun 28 16:45:35 2021

@author: Anindita
"""

test_str = input("Enter the string: ")
  
print("The original string is : " + str(test_str))
  
res = ''.join(format(ord(i), '08b') for i in test_str)
  
print("The string after binary conversion : " + str(res))

a=[]

a=str(res[::2])
modified_even = res[::2]
#print("Even string: ",modified_even)
first_half  = a[0:len(a)//2]
second_half = a[len(a)//2 if len(a)%2 == 0 else ((len(a)//2)+1):]
#print(first_half)
#print(second_half)
encrypt=(first_half+str(res)+second_half)
print("Concatenated encrypted string: ",encrypt)
cut1=encrypt[6:]
cut2=cut1[:-6]
#print(cut1)
print("Decrpyted string in binary is: ",cut2)

def decode1(str):
    message = ""
    while str != "":
        i = chr(int(str[:8], 2))
        message = message + i
        str = str[8:]
    return message

print("Decrypted main string: ",decode1(cut2))


