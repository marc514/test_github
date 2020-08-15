# coding: utf-8

###########################################
# Copyright© All Rights Reserved.
# @Brief: 
# @Auther: 
# @Email: 
# @Date: 20200730
###########################################

# tcp client sockerserver

from socket import *
from time import *

HOST = gethostname() 
PORT = 23456
BUFSIZ = 1024
ADDR = (HOST, PORT)

# SocketServer 请求处理程序的默认行为是接受连接、获取请求，然后关闭连接。
# 由于这个原因，我们不能在应用程序整个执行过程中都保持连接，
# 因此每次向服务器发送消息时，都需要创建一个新的套接字。
# tcpCliSock = socket(AF_INET, SOCK_STREAM)
# tcpCliSock.connect(ADDR)

while True:
    tcpCliSock = socket(AF_INET, SOCK_STREAM)
    tcpCliSock.connect(ADDR)
    data2send = input('> ')
    if not data2send:
        break
    tcpCliSock.send(('client发送时间 {}\t{}\n'
                    .format(time(), data2send))
                    .encode('utf-8')) 
    data = tcpCliSock.recv(BUFSIZ)
    if not data:
        break
    print ('{}\nclient接受时间 {}'
            .format(data.decode('utf-8'), time()))
    tcpCliSock.close()