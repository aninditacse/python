# -*- coding: utf-8 -*-
"""
Created on Wed Jun 23 10:39:48 2021

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
        ns = Pyro4.locateNS(host=self.host,port=self.port) # find the name server)
        server_names = ns.list('rmiserver-') #this should be returning me all servers registered on pyro's nameserver
        keys = list(server_names.keys())

        for key in keys:
            each_server = Pyro4.Proxy(server_names[key])
            try:
                each_server.receiveMessageToReplica(name_server, message)
            except Pyro4.errors.CommunicationError:
                print('Can\'t send message to server ' + key.split('rmiserver-')[1])

    def add_num(self,message1,message2):
        print('Someone called my addition method :)')
        sum1=message1+message2
        sum2=sum1
        
        
        
      
        return "Addition of "+str(message1)+" and "+str(message2)+" is "+str(sum2)+self.prime(sum1)
        
    
    
    def prime(self,sum1):
        print('Someone called my prime checking method :)')
        if sum1>1:
            for i in range(2,int(sum1/2)+1):
                if(sum1%i==0):
                    return " and the sum is not a prime number "
                else:
                    return " and the sum is a prime number"
        
        
    
    