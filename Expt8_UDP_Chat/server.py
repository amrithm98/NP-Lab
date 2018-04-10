import socket

sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
sock.bind(('127.0.0.1',3000))

while True:
	data,address = sock.recvfrom(4096)
	print(data)
	if data:
		sent = sock.sendto(data,address)
		print("Data Sent Back To ",address)

