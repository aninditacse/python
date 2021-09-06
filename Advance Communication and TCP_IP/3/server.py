# -*- coding: utf-8 -*-
"""
Created on Wed Jun 23 14:39:03 2021

@author: Anindita
"""

import socket
import sys

def stringlen(rcvdData):   

    return "String recieved by server is - "+str(rcvdData)+" and the length of the string is "+str(len(rcvdData))   

HOST = ''	
PORT = 8888	

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print ('Socket created')

try:
	s.bind((HOST, PORT))
except socket.error as msg:
	print ('Bind failed. Error Code : ' + str(msg[0]) + ' Message ' + msg[1])
	sys.exit()
	
print ('Socket bind complete')

s.listen(10)
print ('Socket now listening')

conn, addr = s.accept()
print ('Connected with ' + addr[0] + ':' + str(addr[1]))
rcvdData = conn.recv(4096).decode()
print ("Client:",rcvdData)  
  
sendData = stringlen(rcvdData)
print("Server: Length of the string is sent to client")
conn.send(sendData.encode())
	
conn.close()