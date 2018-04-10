import socket
import sys

sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
sock.connect(('192.168.1.102',3000))

while True:
	try:
		msg = raw_input()
		sock.sendall(msg)
		amount_received = 0
		amount_expected = len(msg)

		while amount_received < amount_expected:
			buff = sock.recv(16)
			amount_received += len(buff)
			print("Packet Sent")
	finally:
		pass
