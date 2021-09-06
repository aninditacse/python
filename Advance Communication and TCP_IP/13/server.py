# -*- coding: utf-8 -*-
"""
Created on Tue Jun 22 21:50:38 2021

@author: Anindita
"""

# -*- coding: utf-8 -*-
"""
Created on Tue Jun 22 20:05:01 2021

@author: Anindita
"""

import Pyro4
from rmiechoserver import RMIEchoServer
import sys

HOST='localhost'
PORT=9090

if len(sys.argv) == 2 or len(sys.argv) > 3:
	print('''
If you want to connect to a specific server you need to inform host and port.
Ex: python client.py localhost 9090
Or just run "$ python client.py" to use the default settings.
''')
	exit()

if len(sys.argv) == 3:
	HOST = sys.argv[1]
	try:
		PORT = int(sys.argv[2])
	except ValueError:
		print('%s is a invalid value for port.' % sys.argv[2])
		exit()

name_server = ''

while name_server.strip() == '':
    name_server = input('Insert server name: ')

rmiEchoServer = RMIEchoServer(name_server,HOST,PORT)

daemon = Pyro4.Daemon() 
try:
    ns = Pyro4.locateNS(host=HOST,port=PORT)
    server_names = ns.list('rmiserver-') 
    keys = list(server_names.keys())

    for key in keys:
        each_server = Pyro4.Proxy(server_names[key])

        if key.split('rmiserver-')[1] == name_server:
            continue

        try:
            responseMessage = each_server.getMessages()
            rmiEchoServer.aMessages = responseMessage[1]
            rmiEchoServer.aMessages = responseMessage[2]
            print('Server %s send me %d messages.' % (responseMessage[0], len(responseMessage[1],responseMessage[2]) ) ) 
            break
        except Pyro4.errors.CommunicationError:
            print('Can\'t get messages from server ' + key.split('rmiserver-')[1])

    uri = daemon.register(rmiEchoServer) 
    ns.register('rmiserver-' + name_server, uri) 
    print("Ready.")
    daemon.requestLoop() 

except Pyro4.errors.NamingError:
    print("\nFailed to locate the nameserver on %s:%d. Make sure it's running, execute: \n\npyro4-ns -n %s -p %d\n" % (HOST,PORT,HOST,PORT) )
    exit()