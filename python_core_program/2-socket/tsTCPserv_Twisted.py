# coding: utf-8

###########################################
# Copyright© All Rights Reserved.
# @Brief: 
# @Auther: 
# @Email: 
# @Date: 20200803
###########################################

# tcp server Twisted Reactor

from twisted.internet import protocol, reactor
from time import *

PORT = 23456

class TSServProtocol(protocol.Protocol):
    def connectionMade(self):
        clnt = self.clnt = self.transport.getPeer().host
        print('...connected from: ', clnt)
    
    def dataReceived(self, data):
        self.transport.write('{} {}'
                .format(ctime(),data.decode('utf-8'))
                .encode('utf-8'))

factory = protocol.Factory()
factory.protocol = TSServProtocol
print('waiting for connection...')
reactor.listenTCP(PORT, factory)
reactor.run()