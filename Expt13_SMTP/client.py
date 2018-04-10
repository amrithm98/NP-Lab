import socket
import sys
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect(("127.0.0.1",6000))
print s.recv(1024)
st1=sys.argv[1]
s.send(st1)
st1=s.recv(1024)
if st1=="1":
	st2=sys.argv[2]
	# s.send(st2)
	print "======Connection Establishment======"
	st3=s.recv(1024)
	print "s : "+ st3
	if st3:
		msg=raw_input("HELO ")
		s.send(msg)
		st=s.recv(1024)
		print "s : "+st
		print "======Mail Transfer=========="
		st=raw_input("MAIL FROM : ")
		s.send(st)
		st=s.recv(1024)
		print st + " "
		if st=="1":
			s.send("hai")
			st=s.recv(1024)
			print st
			st=raw_input("RECPT TO : ")
			s.send(st)
			st=s.recv(1024)
			print "s : "+st
			gt=st.split(" ")
			# print gt[0]
			if gt[0]=="421":
				quit()
			# st=raw_input("DATA : ")
			else:
				print "DATA "
				s.send("DATA ")
				lt=s.recv(1024)
				print lt
				st=s.recv(1024)
				print st
				# tt=s.recv(1024)
				if st=="1":
					temp=raw_input("Message: ")
					s.send(temp)
		elif st=="0":
			st=s.recv(1024)
			print "s : "+st
else:
	print "Not valid mail id"
# s.close()
