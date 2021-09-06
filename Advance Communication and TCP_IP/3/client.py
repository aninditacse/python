# -*- coding: utf-8 -*-
"""
Created on Wed Jun 23 14:38:19 2021

@author: Anindita
"""

import socket	
import sys	

try:
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
except socket.error:
	print ('Failed to create socket')
	sys.exit()
	
print ('Socket Created')

host = '127.0.0.1';
port = 8888;

try:
	remote_ip = socket.gethostbyname( host )

except socket.gaierror:
	
	print ('Hostname could not be resolved. Exiting')
	sys.exit()

s.connect((remote_ip , port))

print ('Socket Connected to ' + host + ' on ip ' + remote_ip)

try :
    str = input("Client: ")
    s.send(str.encode())
    print ("Server:",s.recv(1024).decode())
	     
except socket.error:
	print ('Send failed')
	sys.exit()

s.close()