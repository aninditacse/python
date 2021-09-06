# -*- coding: utf-8 -*-
"""
Created on Tue Jun 22 20:04:22 2021

@author: Anindita
"""

import Pyro4
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

def tryToUseMethodAnyServer(method, *args):

	try:
		ns = Pyro4.locateNS(host=HOST,port=PORT)
		server_names = ns.list('rmiserver-') 
		keys = list(server_names.keys())
	except Pyro4.errors.NamingError:
		print("\nFailed to locate the nameserver on %s:%d. Make sure it's running, execute: \n\npyro4-ns -n %s -p %d\n" % (HOST,PORT,HOST,PORT) )
		return False

	for key in keys:
		each_server = Pyro4.Proxy(server_names[key])

		try:
			return getattr(each_server, method)(*args)
		except Pyro4.errors.CommunicationError:
			pass
	
	print("Can't find any server available.")
	return False

while True:
    print ("#-----------------------------------------#")
    print ("#               MENU APP                  #")
    print ("# Options:                                #")
    print ("# [1] Give Input                       #")
    print ("# [0] Exit                                #")
    print ("#-----------------------------------------#")
    try:
        option = input("Choose an option: ")
    except KeyboardInterrupt:
        print('\nThe connection was finished successfully...')
        break
    if option == "1":
        try:
            message1 = int(input("Enter number 1: "))
            message2 = int(input("Enter number 2: "))
        except KeyboardInterrupt:
            print('\nThe connection was finished successfully...')
            break
        returnedMessage = tryToUseMethodAnyServer('add_num', message1,message2)
        if returnedMessage:
            print(returnedMessage)
    
    elif option == "0":
        print('The connection was finished successfully...')
        break
    else:
        print('Option not available.')
    input('Press Enter to continue...')