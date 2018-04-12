import os
import socket
import _thread
import sys

host = sys.argv[1]
port = sys.argv[2]

sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
sock.connect((host,int(port)))

path = os.path.abspath(".")

#Function that gets the list of files in a directory and converts it to a string
def listFiles(path):

	ls = os.listdir(path)
	ans = ""
	for i in ls:
		ans += i + "\n"
	return ans

#Function that reads a file from the directory and returns a string
def readFile(fileName):

	content = ""
	with open(fileName,'r') as f:
		content += f.read()
	return content

#Function that creates a file and writes contents onto it
def writeFile(fileName,data):

	with open(fileName,"w+") as f:
		f.write(data)

#Function that listens to incoming messages from the server and echoes it on to the screen
def listening():
	while True:
		data = sock.recv(300).decode()
		if(data):
			print(data)
			data = data.split()
			if(len(data) >=2):
				msg = ""
				if(data[0] == "get"):
					for i in data[2:]:
						msg += (i + " ")
				writeFile(path+"/"+data[1],msg)	
			print("ftp > ")


#Start a listening thread for each client
_thread.start_new_thread(listening,())

while True:
	print ("ftp > ")
	
	command = input()

	if("quit" in command):
		sock.send("quit".encode())
		quit()

	if("!" in command):

		if("ls" in command):
			print(listFiles(path))

		elif("cd" in command):
			cd = command.split()[1]

			if(cd == ".."):

				dirs = path.split('/')
				newPath = ""
				for i in range(len(dirs)-1):
					newPath += ("/"+dirs[i])

				path = newPath
				print("Path Changed to "+path)

			else:

				tempPath =  path+"/"+cd
				if(os.path.exists(tempPath)):
					path = tempPath
					print("Path Changed to "+path)
				else:
					print("Invalid Directory to Change")

		elif("pwd" in command):
			print(path)

	elif("put" in command):
		fileName = command.split()[1]
		filePath = path+"/"+fileName
		if(not os.path.exists(filePath)):
				print(fileName+":no such file").encode()
		else:
			data = readFile(fileName)
			print("\nData in File :"+data)
			command += (" "+data)
			sock.send(command.encode())

	else:
		sock.send(command.encode())