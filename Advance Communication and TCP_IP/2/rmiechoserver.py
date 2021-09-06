# -*- coding: utf-8 -*-
"""
Created on Wed Jun 23 14:02:25 2021

@author: Anindita
"""

import Pyro4

@Pyro4.expose
class RMIEchoServer(object):

    def __init__(self, name_server, host='localhost', port=9090):
        self.aMessages = list()
        self.name_server = name_server
        self.host = host
        self.port = port

    def sendMessageToReplicas(self, name_server, message):
        ns = Pyro4.locateNS(host=self.host,port=self.port) 
        server_names = ns.list('rmiserver-') 
        keys = list(server_names.keys())

        for key in keys:
            each_server = Pyro4.Proxy(server_names[key])
            try:
                each_server.receiveMessageToReplica(name_server, message)
            except Pyro4.errors.CommunicationError:
                print('Can\'t send message to server ' + key.split('rmiserver-')[1])


    def multiply(self,message1,message2):
        print('Someone called my multiplication method :)')
        mult=message1*message2
        mult1=mult
        return "Multiplication of "+str(message1)+" and "+str(message2)+" is "+str(mult1)+self.oddeven(mult1)
        
    
    
    def oddeven(self,mult):
        print('Someone called my even-odd checking method :)')
        if (mult%2==0):
            return " and the multiplication is an even number"
        else:
            return " and the multiplication is a odd number"