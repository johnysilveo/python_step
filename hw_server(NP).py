import socket

HOST = '127.0.0.1'
PORT = 8888

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as srv:
    srv.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    srv.bind((HOST, PORT))

    srv.listen()
    print(f'Listening on {HOST} : {PORT}')

    conn,addr = srv.accept()

    with conn:
        print("Connected: ",addr)
        while True:
            data = conn.recv(4096)
            if not data:
                break
            conn.sendall(data)

