# -*- coding: utf-8 -*-
"""
Created on Wed Jun 23 00:14:42 2021

@author: Anindita
"""

# -*- coding: utf-8 -*-
"""
Created on Tue Jun 22 21:49:02 2021

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

    def add_num(self,message1):
        print('Someone called my concatenation method :)')
        print("String recieved from client side is - "+str(message1))
        p="World Cup"

        return "Output is: "+str(message1)+str(p)