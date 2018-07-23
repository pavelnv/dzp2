import socket

sock = socket.socket()

sock.bind( ('', 9090) )

sock.listen(1)

while True:
    client, addr = sock.accept()
    print(f"Получен запрос на соединение от (addr)")
