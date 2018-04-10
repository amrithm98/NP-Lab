import sys
import thread
import socket
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
port=5008
host="127.0.0.1"
def listening(server):
	msg=''
	while True:
		data=server.recv(1024)
		print data

s.connect((host,port))
name=raw_input()
s.send(name)
data=s.recv(1024)
print data

thread.start_new_thread(listening,(s,))
while True:
	msg=raw_input()
	s.send(msg)
s.close()
quit()

