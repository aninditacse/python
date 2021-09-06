# -*- coding: utf-8 -*-
"""
Created on Wed Jun 23 14:47:41 2021

@author: Anindita
"""

import socket	
import sys	

try:
	s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
except socket.error:
	print ('Failed to create socket')
	sys.exit()

host = 'localhost';
port = 8888;

try :
    msg=input('Enter string : ')
	
    s.sendto(msg.encode(), (host, port))
    t=s.recvfrom(1024)
   
    print ('Server reply : ' ,t[0].decode())
		

	
except socket.error as msg:
    print ('Error Code : ' + str(msg[0]) + ' Message ' + msg[1])
    sys.exit()
s.close()