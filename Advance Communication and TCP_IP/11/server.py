# -*- coding: utf-8 -*-
"""
Created on Mon Jun  7 19:45:07 2021

@author: Anindita
"""

import socket

  
     

s = socket.socket()
port = 12345
s.bind(('', port))
s.listen(5)
c, addr = s.accept()
print ("Socket Up and running with a connection from",addr)
#while True:
rcvdData1 = c.recv(1024).decode()
rcvdData2=c.recv(1024).decode()
print ("Client:",rcvdData1)
print ("Client:",rcvdData2)
p='INDIA2015'
x=rcvdData1+rcvdData2+p
#print('Concatenated String =',x)
#l=len(rcvdData)   
sendData = x
print("Server: Concatenated string is sent")
c.send(sendData.encode())
#    if(sendData == "Bye" or sendData == "bye"):
#        break
c.close()