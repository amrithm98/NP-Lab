import socket
import datetime
import time

sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
sock.bind(('127.0.0.1',3006))

while True:
	data,address = sock.recvfrom(100)
	print("Recieved Time from "+str(address)+" is "+str(data))
	if data:
		time.sleep(1)
		msg = str(datetime.datetime.now().time())[0:8]
		sent = sock.sendto(msg,address)
		print("Time Sent Back To ",address)

