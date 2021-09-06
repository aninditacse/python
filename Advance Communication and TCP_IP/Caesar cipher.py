# -*- coding: utf-8 -*-
"""
Created on Sun Jun  6 20:39:46 2021

@author: Anindita
"""

def encrypt(string, shift):
 
  cipher = ''
  for char in string:
    if char == ' ':
      cipher = cipher + char
    elif  char.isupper():
      cipher = cipher + chr((ord(char) + shift - 65) % 26 + 65)
    else:
      cipher = cipher + chr((ord(char) + shift - 97) % 26 + 97)
  
  return cipher
 
text = input("Enter a string: ")
s = int(input("Enter shift number: "))
print("Original string: ", text)
print("After encryption: ", encrypt(text, s))