import socket
import datetime
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.bind(("127.0.0.1",6000))
x=[]
x.append("amrith@gmail.com")
x.append("anand@gmail.com")
s.listen(5)
conn,addr=s.accept()
conn.send("Trying to connect.....")
mail=conn.recv(1024)
fl=0
fl1=0
fl2=0
print mail
for i in x:
	if mail==i:
		conn.send("1")
		fl=1
		break
	else:
		conn.send("0")
if fl==1:
	msg="220 "+mail+" SMTP Server ready "+str(datetime.datetime.now())
	conn.send(msg)
	st=conn.recv(1024)
	msg="250 "+st
	conn.send(msg)
	st=conn.recv(1024)
	msg="250 Sender <"+st+">"
	for i in x:
		if i==st:
			conn.send("1")
			tt=conn.recv(1024)
			if tt=="hai":
				conn.send(msg)
				fl1=1
				break
	if fl1==0:
		conn.send("0")
		conn.send("421 Service is not available ")
	st=conn.recv(1024)
	to=st
	for i in x:
		if i==to:
			fl2=1
	if fl2==1:
		msg="250 RECEPIENT <"+st+">"
		conn.send(msg)
	else:
		conn.send("421 Service is not available")
	if fl2==1:
		msg=conn.recv(1024)
		# print msg
		conn.send("354 ok send data ending with <CRLF>.<CRLF>")
		inp=open(st,"w+")
		conn.send("1")
		buff=conn.recv(2048)
		print buff
		inp.write(buff)
# port=conn.recv(1024)
# print port
