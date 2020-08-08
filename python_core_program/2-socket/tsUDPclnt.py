# coding: utf-8

###########################################
# Copyright© All Rights Reserved.
# @Brief: 
# @Auther: 
# @Email: 
# @Date: 20200730
###########################################

# udp client
# cs = socket() # 创建客户端套接字
# comm_loop: # 通信循环
#     cs.sendto()/cs.recvfrom() # 对话（发送/接收）
# cs.close() # 关闭客户端套接字

from socket import *
from time import *

HOST = '10.34.37.3'
PORT = 23458
BUFSIZ = 1024
ADDR = (HOST, PORT)

udpCliSock = socket(AF_INET, SOCK_DGRAM)

while True:
    data2send = input('> ')
    if not data2send:
        break
    udpCliSock.sendto(('{}\n{}'.format(time(), data2send))\
                    .encode('utf-8'), ADDR)  # client发送时间
    data, ADDR = udpCliSock.recvfrom(BUFSIZ)
    if not data:
        break
    print (data.decode())
    print (time())  # client接受时间

udpCliSock.close()