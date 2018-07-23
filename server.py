import socket

sock = socket.socket()

sock.bind(('', 9040))

sock.listen(1)

while True:
    client, addr = sock.accept()
    print(f"Получен запрос на соединение от (str(addr))")
    client.send('Hello world!'.encode("utf-8"))
    client.close()