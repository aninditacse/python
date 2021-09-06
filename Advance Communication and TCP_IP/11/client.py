# -*- coding: utf-8 -*-
"""
Created on Mon Jun  7 19:46:04 2021

@author: Anindita
"""

import socket

s = socket.socket()
s.connect(('127.0.0.1',12345))
#while True:
str = input("Client: Enter first string ")
str1=input("Client: Enter second string ")
s.send(str.encode())
s.send(str1.encode())
#    if(str == "Bye" or str == "bye"):
#        break
print ("Server:",s.recv(1024).decode())
#if(str == "Bye" or str == "bye"):
#    break
s.close()