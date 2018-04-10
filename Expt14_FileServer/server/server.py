import socket
import sys
import os

sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
sock.bind(('127.0.0.1',3004))
sock.listen(1)

while True:
	connection,client = sock.accept()
	try:
		while True:
			fileName = connection.recv(16)

			if fileName:
				#If File exists
				if(os.path.exists(fileName)):
					connection.sendall("1")
					oper = connection.recv(5)
					if(oper == "get"):
						content = ""
						with open(fileName,'r') as f:
							content = f.read()
						connection.sendall(content)
				else:
					#Send PID. (It's in the question :P)
					connection.sendall(str(client[1]))
					oper = connection.recv(5)
					if(oper == "put"):
						buff = connection.recv(300)
						print(buff)
						f = open(fileName,"a+")
						f.write(buff)
						f.close()
						connection.sendall("1")
			else:
				print("No Requests From Client")
				break
	finally:
		connection.close()
