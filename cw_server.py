import asyncio  # stdlib for async I/O

HOST = "127.0.0.1"  # bind address (localhost)
PORT = 8888         # TCP port to listen on
clients=[]
async def handle(reader: asyncio.StreamReader, writer: asyncio.StreamWriter):  # per-connection coroutine
    peer = writer.get_extra_info("peername")  # client's (ip, port)
    print("Connected:", peer)  # log new connection
    try:
        while True:  # read multiple lines from this client
            line = await reader.readline()  # await one line (ends with '\n'); b'' on EOF
            if not line:  # EOF -> client closed socket
                break  # exit loop for this client
            text = line.rstrip(b"\r\n").decode("utf-8", errors="replace")  # strip CR/LF and decode safely
            writer.write(f"you said: {text}\n".encode("utf-8"))  # enqueue reply with newline
            await writer.drain()  # flush kernel send buffer (backpressure-aware)
    except asyncio.CancelledError:  # task cancelled (e.g., server shutdown)
        raise  # propagate cancellation
    except Exception as e:  # unexpected runtime error
        print("Error with", peer, e)  # log error and keep server running
    finally:
        writer.close()  # initiate half-close for writing
        await writer.wait_closed()  # wait until socket fully closed
        print("Closed:", peer)  # log disconnect

async def main():  # main entrypoint for the server
    server = await asyncio.start_server(handle, HOST, PORT, backlog=100)  # create TCP server
    sock = server.sockets[0] if server.sockets else None  # get listening socket (if any)
    if sock:  # when bound OK
        host, port = sock.getsockname()[:2]  # actual bound host/port
        print(f"Listening on {host}:{port}")  # log listening address
    async with server:  # ensure clean shutdown context
        await server.serve_forever()  # handle clients until cancelled

if __name__ == "__main__":  # run via `python server_async.py`
    try:
        asyncio.run(main())  # start event loop and run server
    except KeyboardInterrupt:
        print("\nShutting down.")  # graceful Ctrl+C message
