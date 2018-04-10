import socket

sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
server = ('127.0.0.1',3000)
n = 0
try:

	while n == 0:
		msg = raw_input("Enter Data: ")
		sent = sock.sendto(msg,server)
		print("Waiting for resp")
		data,server = sock.recvfrom(4096)
		print("Received Data: "+data)
		n=input("1 to exit or 0 to continue")
		if(n == 1):
			break
finally:
	sock.close()

