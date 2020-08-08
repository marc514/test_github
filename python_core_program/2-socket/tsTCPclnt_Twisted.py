# coding: utf-8

###########################################
# Copyright© All Rights Reserved.
# @Brief: 
# @Auther: 
# @Email: 
# @Date: 20200803
###########################################

# tcp client Twisted Reactor

from twisted.internet import protocol, reactor
from time import *

HOST = '10.34.37.3'
PORT = 23456

class TSClntProtocol(protocol.Protocol):
    def sendData(self):
        data = input('> ')
        if data:
            print('...sending: {}'.format(data))
            self.transport.write(data.encode('utf-8'))
        else:
            self.transport.loseConnection()
    
    def connectionMade(self):
        self.sendData()
    
    def dataReceived(self, data):
        print (data.decode('utf-8'))
        self.sendData()
    
class TSClntFactory(protocol.ClientFactory):
    protocol = TSClntProtocol
    clientConnectionLost = clientConnectionFailed = \
        lambda self, connector, reason: reactor.stop()
        # == 定义lambda函数: 
        # def func_lambda(self, connector, reason):
        #     reactor.stop()

reactor.connectTCP(HOST, PORT, TSClntFactory())
reactor.run()