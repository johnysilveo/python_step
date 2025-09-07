import asyncio

HOST = "127.0.0.1"
PORT = 8888

async def listen(reader):
    while True:
        line = await reader.readline()
        if not line:
            break
        print(line.decode().strip())

async def main():
    reader, writer = await asyncio.open_connection(HOST, PORT)
    asyncio.create_task(listen(reader))

    try:
        while True:
            msg = input("> ")   # команди: start, stop, restart, або число 1–9
            writer.write((msg + "\n").encode())
            await writer.drain()
    except KeyboardInterrupt:
        print("Bye")
        writer.close()
        await writer.wait_closed()

if __name__ == "__main__":
    asyncio.run(main())
