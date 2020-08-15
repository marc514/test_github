# coding: utf-8

###########################################
# Copyright© All Rights Reserved.
# @Brief: 
# @Auther: 
# @Email: 
# @Date: 20200730
###########################################

# udp server
# ss = socket() # 创建服务器套接字
# ss.bind() # 绑定服务器套接字
# inf_loop: # 服务器无限循环
#     cs = ss.recvfrom()/ss.sendto() # 关闭（接收/发送）
# ss.close() # 关闭服务器套接字

from socket import *
from time import *

HOST = ''
PORT = 23458
BUFSIZ = 1024
ADDR = (HOST, PORT)

udpSerSock = socket(AF_INET, SOCK_DGRAM)
udpSerSock.bind(ADDR)

while True:
    print ('waiting for message...')
    data, addr = udpSerSock.recvfrom(BUFSIZ)
    udpSerSock.sendto(('{}\n{}'.format(data.decode('utf-8'), time())) \
                        .encode('utf-8'), addr)
    print ('...recieved from and return to:', addr)

udpSerSock.close()