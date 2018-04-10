import socket

sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
sock.bind(('',3002))
sock.listen(1)

while True:
    conn,client = sock.accept()
    if conn:
        try:
            while True:
                data = conn.recv(10)
                if data:
                    print("Got data "+data.decode())
                    data = input()
                    conn.send(data.encode())
                else:
                    print("Empty")
                    break
        finally:
            conn.close()
