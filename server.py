import socket
import json

sock = socket.socket()

sock.bind(('', 9090))

sock.listen(1)

data = {
    "msg": "Hello",
    "action": 'do smth'
}

s_data = json.dumps(data)

while True:
    client, addr = sock.accept()
    print(f"Получен запрос на соединение от {str(addr)}")
    client.send(s_data.encode("utf-8"))
    client.close()