import socket

sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
sock.bind(('',3004))

while True:
    data,addr = sock.recvfrom(100)
    if data:
        print(data.decode())
        sock.sendto("Got it".encode(),addr)
    else:
        break