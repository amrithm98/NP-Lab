import socket
import _thread

sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
sock.bind(('',3003))
sock.listen(10)


def SMTP(conn,client):
    i = 0
    expected = ["helo","mail to","rcpt to","data","send","quit"]
    reply = conn.recv(100).decode()
    print(reply)
    if(reply in expected[i]):
        i += 1
        conn.send("s : 250 OK\n".encode())
        reply = conn.recv(100).decode()
        print(reply)
    else:
        conn.send("s : 500 Unexpected Command\n".encode())
        continue


while True:
    conn,client = sock.accept()
    _thread.start_new_thread(SMTP,(conn,client))
