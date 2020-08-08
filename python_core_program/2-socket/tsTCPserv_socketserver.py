# coding: utf-8

###########################################
# Copyright© All Rights Reserved.
# @Brief: 
# @Auther: 
# @Email: 
# @Date: 20200730
###########################################

# tcp server sockerserver

from socketserver import (TCPServer as TCP, 
                StreamRequestHandler as SRH)
from time import *

HOST = ''
PORT = 23456
# BUFSIZ = 1024
ADDR = (HOST, PORT)

class MyRequestHandler(SRH):
    def handle(self):
        print('...connected from:', self.client_address)
        self.wfile.write(('{}server发送时间 {}'
            .format(self.rfile.readline().decode(), 
                    time())).encode('utf-8'))

tcpServ = TCP(ADDR, MyRequestHandler)
print('waiting for connection...')
tcpServ.serve_forever()