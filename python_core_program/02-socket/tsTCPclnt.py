# coding: utf-8

###########################################
# Copyright© All Rights Reserved.
# @Brief: 
# @Auther: 
# @Email: 
# @Date: 20200730
###########################################

# tcp client
# cs = socket() # 创建客户端套接字
# cs.connect() # 尝试连接服务器
# comm_loop: # 通信循环
#     cs.send()/cs.recv() # 对话（发送/接收）
# cs.close() # 关闭客户端套接字

from socket import *
from time import *

HOST = gethostname() 
PORT = 23456
BUFSIZ = 1024
ADDR = (HOST, PORT)

tcpCliSock = socket(AF_INET, SOCK_STREAM)
tcpCliSock.connect(ADDR)

while True:
    data2send = input('> ')
    if not data2send:
        break
    tcpCliSock.send(('{}\n{}'.format(time(), data2send)) \
                    .encode('utf-8'))  # client发送时间
    data = tcpCliSock.recv(BUFSIZ)
    if not data:
        break
    print (data.decode('utf-8'))
    print (time())  # client接受时间
tcpCliSock.close()