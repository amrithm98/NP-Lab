import socket
import _thread

sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
sock.connect(('',3003))

def listening():
    while True:
        data = sock.recv(100)
        print(data.decode())

name = input()
name = name.encode()
sock.send(name)
welcome = sock.recv(100)
print(welcome.decode())

_thread.start_new_thread(listening,())

while True:
    data = input()
    sock.send(data.encode())