import socket
import sys

sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
sock.bind(('',3000))
sock.listen(1)

while True:
	connection,client = sock.accept()
	try:
		print("Client is : ",client)
		while True:
			buff = connection.recv(16)
			print("Received Data : ",buff)
			if buff:
				print("Writing Data Back To Client")
				connection.sendall(buff)
			else:
				print("Empty Buffer")
				break
	finally:
		connection.close()
