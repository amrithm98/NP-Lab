import socket
sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
sock.connect(('',3002))

while True:
    data = input()
    sock.send(data.encode())
    b = sock.recv(10)
    print(b.decode())
