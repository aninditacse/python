# -*- coding: utf-8 -*-
"""
Created on Wed Jun 23 14:48:21 2021

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
    data = d[0].decode()
    addr = d[1]
    res = data.upper()
    concati= res+'RR2014'
    print("Capitalized string is sent to client")
    s.sendto(concati.encode(),addr)
        
except socket.error as msg:
    print ('Error Code : ' + str(d[0]) + ' Message ' + d[1])
    sys.exit()
	
s.close()