# -*- coding: utf-8 -*-
"""
Created on Sun Jun 13 17:29:53 2021

@author: Anindita
"""

import socket
import sys


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
sendData = rcvdData.upper()
print("Server: Uppercase string is sent to the client")
conn.send(sendData.encode())
	
conn.close()