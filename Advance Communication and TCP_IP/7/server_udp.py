# -*- coding: utf-8 -*-
"""
Created on Sun Jun 20 09:49:16 2021

@author: Anindita
"""

import socket
import sys

HOST = ''	
PORT = 8888	

try :
	s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
	print ('Socket created')
except socket.error as msg :
	print ('Failed to create socket. Error Code : ' + str(msg[0]) + ' Message ' + msg[1])
	sys.exit()

try:
	s.bind((HOST, PORT))
except socket.error as msg:
	print ('Bind failed. Error Code : ' + str(msg[0]) + ' Message ' + msg[1])
	sys.exit()
	
print ('Socket bind complete')

try:
    d = s.recvfrom(1024)
    data = d[0]
    addr = d[1]
    res = data.title()
    print("Capitalized string is sent to client")
    s.sendto(res,addr)
    
except socket.error as msg:
    print ('Error Code : ' + str(d[0]) + ' Message ' + d[1])
    sys.exit()
	
s.close()