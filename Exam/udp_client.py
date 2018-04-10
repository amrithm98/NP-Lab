import socket

sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
server = ('',3004)

while True:
    data = input().encode()
    sock.sendto(data,server)
    data,addr = sock.recvfrom(100)
    print(data)