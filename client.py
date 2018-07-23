import socket

sock = socket.socket()

sock.connect(('localhost', 9040))

while True:
    data = sock.recv(1024)
    if len(data) == 0:
        break

    print(data.decode("utf-8"))

sock.close()