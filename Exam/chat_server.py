import socket
import _thread

sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
sock.bind(('',3003))
sock.listen(10)

connected = []

def client(conn,addr):
    name = conn.recv(100)
    name = name.decode()
    print(name + " Joined Chat")
    conn.sendall("Welcome to Chat Room".encode())
    while True:
        data = conn.recv(100)
        if data:
            data = data.decode()
            print(name + " => " + data)
            msg = name + " => " + data
            broadCast(conn,msg.encode())
        else:
            break
    conn.close()

def broadCast(conn,data):
    for client in connected:
        if(client != conn):
            try:
                client.sendall(data)
            except:
                client.close()
                connected.remove(client)


while True:
    conn,cnt = sock.accept()
    connected += [conn]
    _thread.start_new_thread(client,(conn,cnt))
