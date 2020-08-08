import socket

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
serverIP = '10.202.91.88'
serverPort = 62493
s.bind((serverIP,serverPort))

while True:
	data,addr = s.recvfrom(2048)
	if not data:
		print ("client dont exist")
		break
	print ("rece:",data,"from:",addr)
s.close()