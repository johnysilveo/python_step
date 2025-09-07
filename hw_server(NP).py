# import socket
#
# HOST = '127.0.0.1'
# PORT = 8888
#
# # def send_massage(conn):
# #     while True:
# #         msg = input('>')
# #         if msg.lower() == 'exit':
# #             break
# #         conn.sendall(msg.encode('utf-8'))
# #
# # with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as srv:
# #     srv.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
# #
# #     srv.bind((HOST, PORT))
# #
# #     srv.listen()
# #     print(f'Listening on {HOST} : {PORT}')
# #
# #     conn,addr = srv.accept()
# #
# #     with conn:
# #         print("Connected: ",addr)
# #         while True:
# #             data = conn.recv(4096)
# #             if not data:
# #                 break
# #             conn.sendall(data)
#
#
# def hande(conn):
#     buf = b""
#     while True:
#         chunk = conn.recv(4096)
#         if not chunk:
#             return
#         buf += chunk
#
#         while b"\n" in buf:
#             line,buf = buf.split(b'\n',1)
#             text = line.decode("utf-8", errors="replace")
#             reply = f"you said: {text}\n".encode("utf-8")
#             conn.sendall(reply)
#
# with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as srv:
#     srv.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
#     srv.bind((HOST, PORT))
#     srv.listen()
#     print(f'Listening on {HOST} : {PORT}')
#     while True:
#         conn,addr = srv.accept()
#         with conn:
#             hande(conn)
#         print('Disconnected')



import asyncio

HOST = "127.0.0.1"
PORT = 8888

clients = []  # список з'єднань (writer)

BOARD_TEMPLATE = """
 {0} | {1} | {2}
---+---+---
 {3} | {4} | {5}
---+---+---
 {6} | {7} | {8}
"""

def format_board(board):
    return BOARD_TEMPLATE.format(*board)

async def broadcast(message: str):
    for client in clients:
        client.write((message + "\n").encode())
        await client.drain()

async def handle_client(reader: asyncio.StreamReader, writer: asyncio.StreamWriter):
    addr = writer.get_extra_info("peername")
    print(f"Connected: {addr}")
    clients.append(writer)

    try:
        while True:
            data = await reader.readline()
            if not data:
                break
            msg = data.decode().strip()
            await process_message(msg, writer)
    finally:
        print(f"Disconnected: {addr}")
        clients.remove(writer)
        writer.close()
        await writer.wait_closed()

# ---------------- game logic ----------------

board = [" "] * 9
game_on = False
turn = 0
players = {}   # writer -> symbol

async def process_message(msg: str, writer: asyncio.StreamWriter):
    global game_on, turn, board, players

    if msg.lower() == "start" and len(clients) == 2 and not game_on:
        # Player who typed "start" becomes X, other is O
        players = {clients[0]: "X", clients[1]: "O"}
        board = [" "] * 9
        game_on = True
        turn = 0
        await broadcast("Game started! Player X goes first.\n" + format_board(board))
        return

    if msg.lower() == "stop" and game_on:
        sym = players.get(writer, "?")
        await broadcast(f"Player {sym} stopped the game. {sym} loses!")
        game_on = False
        return

    if msg.lower() == "restart" and not game_on:
        await broadcast("Type START to begin a new game.")
        return

    # moves
    if game_on and msg.isdigit():
        pos = int(msg) - 1
        if 0 <= pos < 9 and board[pos] == " ":
            current_writer = clients[turn % 2]
            if writer != current_writer:
                writer.write(b"Not your turn!\n")
                await writer.drain()
                return

            symbol = players[writer]
            board[pos] = symbol
            await broadcast(format_board(board))

            if check_winner(board, symbol):
                await broadcast(f"Player {symbol} wins!")
                game_on = False
                return

            if " " not in board:
                await broadcast("Draw!")
                game_on = False
                return

            turn += 1
            next_symbol = players[clients[turn % 2]]
            await broadcast(f"Player {next_symbol}'s turn.")
        else:
            writer.write(b"Invalid move!\n")
            await writer.drain()

def check_winner(b, sym):
    wins = [(0,1,2),(3,4,5),(6,7,8),
            (0,3,6),(1,4,7),(2,5,8),
            (0,4,8),(2,4,6)]
    return any(b[a]==b[b_] == b[c]==sym for a,b_,c in wins)

# ---------------- main ----------------

async def main():
    server = await asyncio.start_server(handle_client, HOST, PORT)
    print(f"Server running on {HOST}:{PORT}")
    async with server:
        await server.serve_forever()

if __name__ == "__main__":
    asyncio.run(main())
