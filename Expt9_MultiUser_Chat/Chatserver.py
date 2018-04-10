import sys
import thread
import socket
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
host="127.0.0.1"
port=5008
cl=[]

def client(conn,addr):
	name=conn.recv(1024)
	print name+" Joined Chat room "
	conn.send("Welcome to chat room")
	while True:
		try:
			data=conn.recv(1024)

			if not data:
				break
			data=name+"=>"+data
			print data
			broad(conn,data)
		except:
			continue
	conn.send('')
	conn.close()

def broad(conn,data):
	for connection in cl:
		if connection!=conn:
			try:
				connection.send(data)
			except:
				conn.close()
				cl.remove(conn)
		else:
			continue
			
s.bind((host,port))
s.listen(10)
while True:
	conn,addr=s.accept()
	cl.append(conn)
	thread.start_new_thread(client,(conn,addr))
quit()

	

