# coding: utf-8

###########################################
# Copyright© All Rights Reserved.
# @Brief: 
# @Auther: 
# @Email: 
# @Date: 20200730
###########################################

# tcp server
# ss = socket() # 创建服务器套接字
# ss.bind() # 套接字与地址绑定
# ss.listen() # 监听连接
# inf_loop: # 服务器无限循环
#     cs = ss.accept() # 接受客户端连接
#     comm_loop: # 通信循环
#         cs.recv()/cs.send() # 对话（接收/发送）
#     cs.close() # 关闭客户端套接字
# ss.close() # 关闭服务器套接字#（可选）

from socket import *
from time import *

HOST = ''
PORT = 23456
BUFSIZ = 1024
ADDR = (HOST, PORT)

tcpSerSock = socket(AF_INET, SOCK_STREAM)
tcpSerSock.bind(ADDR)
tcpSerSock.listen(5)  # 可以挂起的最大连接数量

while True:
    print ('waiting for connecting...')
    tcpCliSock, addr = tcpSerSock.accept()  # 单线程，只能连接一个
    print ('...connected from:', addr)

    while True:
        data = tcpCliSock.recv(BUFSIZ)
        if not data:
            break
        tcpCliSock.send(('{}\n{}'.format(data.decode('utf-8'), time())) \
                        .encode('utf-8'))  # server端发送
    tcpCliSock.close()
tcpSerSock.close()