import socket

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
clientIP = '10.202.91.88'
clientPort = 31593
s.bind((clientIP,clientPort))

while True:
    msg = bytes(input(),"utf-8")
    addr = ('10.202.91.88',62493)
    if not msg:
        break
    s.sendto(msg, addr)
s.close()