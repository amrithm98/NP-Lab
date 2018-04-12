import os
import socket
import _thread
import sys

host = sys.argv[1]
port = sys.argv[2]

sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
sock.bind((host,int(port)))
sock.listen(10)

#Function To Read Contents of a File and Return a String
def readFile(fileName):

	content = ""
	with open(fileName,'r') as f:
		content = f.read()
	return content

#Function to create a file with given contents
def writeFile(fileName,data):

	with open(fileName,"w") as f:
		f.write(data)

#Function to list files and return a string
def listFiles(path):

	ls = os.listdir(path)
	ans = ""
	for i in ls:
		ans += i + "\n"
	return ans

#FTP Function which is executed for every client.
def FTP(conn,addr):

	conn.send("Connected to FTP Server".encode())
	path = os.path.abspath(".")
	print("Server Working for Client "+str(addr)+" at Path "+path)
	while True:

		command = conn.recv(100).decode()
		if("quit" in command):
			quit()

		if(len(command.split()) > 1):
			fileName = command.split()[1]
		else:
			fileName = ""

		if("get" in command):
			filePath = path+"/"+fileName
			if(not os.path.exists(filePath)):
				conn.send((fileName+":no such file").encode())
			else:
				data = readFile(filePath)
				conn.send(("get "+fileName+" "+data).encode())

		elif ("put" in command):
			data = (command.split()[1:])
			msg = ""
			filePath = path+"/"+fileName
			for i in data:
				msg += (i + " ")
			writeFile(filePath,msg)
			conn.send(("Successfully Transferred File to "+path).encode())
			

		elif("cd" in command):

			cd = command.split()[1]

			if(cd == ".."):
				dirs = path.split('/')
				newPath = ""
				for i in range(len(dirs)-1):
					newPath += ("/"+dirs[i])

				path = newPath
				conn.send(("Path Changed to "+path).encode())

			else:
				tempPath =  path+"/"+cd
				if(os.path.exists(tempPath)):
					path = tempPath
					conn.send(("Path Changed to "+path).encode())
				else:
					conn.send("Invalid Directory to Change".encode())


		elif("ls" in command):

			data = listFiles(path)
			conn.send(data.encode())

		elif("pwd" in command):
			conn.send(path.encode())

		else:
			conn.send("An invalid FTP Command".encode())


#List of connected Clients
connected=[]

while True:

	#Accept a connection and Start a New Thread of FTP Function
	conn,addr = sock.accept()
	connected += [conn]
	_thread.start_new_thread(FTP,(conn,addr))