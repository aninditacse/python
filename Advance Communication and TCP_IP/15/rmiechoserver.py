# -*- coding: utf-8 -*-
"""
Created on Wed Jun 23 00:06:46 2021

@author: Anindita
"""

# -*- coding: utf-8 -*-
"""
Created on Tue Jun 22 23:19:35 2021

@author: Anindita
"""

# -*- coding: utf-8 -*-
"""
Created on Tue Jun 22 20:03:07 2021

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

    def echoService(self, message):
        self.sendMessageToReplicas(self.name_server, str(message))
        print('Someone called my echoService :)')
        return self.name_server + ": " + str(message)


    def add_num(self,message1,message2):
        print('Someone called my addition method :)')
        sum1=message1+message2
        mult=message1*message2
        sub=message1-message2
        div=message1/message2
        sum2=sum1
        p=1
        while (sum1!=0):
            p=p*int(sum1%10)
            sum1=int(sum1/10)
      
        return "Addition,Subtruction,Multiplication and Division of "+str(message1)+" and "+str(message2)+" is "+str(sum2)+" , "+str(sub)+" , "+str(mult)+" , "+str(div)+" respectively "+" and multiplication of digits of "+str(sum2)+" is "+str(p)