import socket

HOST = "127.0.0.1"
PORT = 8888

with socket.create_connection((HOST, PORT), timeout=5) as s:
    s.sendall(b'hello dude!\n')
    data = s.recv(1024)
    print('RECV:',data.decode('utf-8', errors='replace'))