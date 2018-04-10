import socket
import sys

sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
sock.connect(('127.0.0.1',3004))

while True:
	try:
		print("\nEnter FileName To Open At Server: ")
		fileName = raw_input()
		sock.sendall(fileName)
		res = sock.recv(5)
		if(res == '1'):
			print("\n1. Open File")
			n = input()
			if(n == 1):
				sock.sendall("get")
				fileData = sock.recv(100)
				print(fileName+"\n===================")
				print(fileData)
			else:
				buff = sock.recv(20)
				print(buff)
		else:
			print("File NOT FOUND "+str(res))
			print("\n2. Send a File")
			n = input()
			if(n == 2):
				sock.sendall("put")
				content = ""
				with open(fileName,'r') as f:
					content = f.read()
				sock.sendall(content)
				resp = sock.recv(1)
				print("Successfully Tranferred File")
			else:
				continue
	finally:
		pass
