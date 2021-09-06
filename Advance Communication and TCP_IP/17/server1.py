# -*- coding: utf-8 -*-
"""
Created on Sun Jun 13 19:19:41 2021

@author: Anindita
"""

import socket
import sys
from num2words import num2words

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
p=num2words(rcvdData, to = 'cardinal')
#sendData =p+'rrworld'
print("Server: Number to word conversion sent to client")
conn.send(p.encode())
	
conn.close()