# -*- coding: utf-8 -*-
"""
Created on Sat Jun 26 17:10:56 2021

@author: Anindita
"""

def vernam(plain_text,key):

    # convert into lower cases and remove spaces
    
    plain_text=plain_text.replace(" ","")
    key=key.replace(" ","")
    plain_text=plain_text.lower()
    key=key.lower()
    
    # conditional statements
    if(len(plain_text)!=len(key)):
        print("Lengths are different")
        
    else:
        cipher_text=""
        
        # iterating through the length
        for i in range(len(plain_text)):
            k1=ord(plain_text[i])-97
            k2=ord(key[i])-97
            s=chr((k1+k2)%26+97)
            cipher_text+=s
        print("Enrypted message is: ",cipher_text)


plain_text=input("Enter the message: ")
key=input("Enter the one time pad: ")
vernam(plain_text,key)