import asyncio

HOST = "127.0.0.1"
PORT = 8888

# minimal hardcoded users
USERS = {"johny": "1234", "anna": "abcd", "mike": "qwerty"}

class ChatServer:
    def __init__(self):
        self.clients: set[asyncio.StreamWriter] = set()
        self.user_by_writer: dict[asyncio.StreamWriter, str] = {}

    async def send(self, w: asyncio.StreamWriter, msg: str):
        w.write((msg + "\n").encode("utf-8"))
        await w.drain()

    async def broadcast(self, msg: str, skip: asyncio.StreamWriter | None = None):
        dead = []
        for w in list(self.clients):
            if w is skip:
                continue
            try:
                w.write((msg + "\n").encode("utf-8"))
                await w.drain()
            except Exception:
                dead.append(w)
        for w in dead:
            self.clients.discard(w)
            self.user_by_writer.pop(w, None)
            try:
                w.close()
                await w.wait_closed()
            except Exception:
                pass

    async def handle_client(self, reader: asyncio.StreamReader, writer: asyncio.StreamWriter):
        addr = writer.get_extra_info("peername")
        username = None
        try:
            await self.send(writer, "Use: LOGIN <user> <pass>")
            line = await reader.readline()
            if not line:
                writer.close(); await writer.wait_closed(); return

            parts = line.decode("utf-8").strip().split()
            if len(parts) < 3 or parts[0].upper() != "LOGIN":
                await self.send(writer, "ERR auth format")
                writer.close(); await writer.wait_closed(); return

            user, pw = parts[1], " ".join(parts[2:])
            if USERS.get(user) != pw:
                await self.send(writer, "ERR bad credentials")
                writer.close(); await writer.wait_closed(); return

            username = user
            self.clients.add(writer)
            self.user_by_writer[writer] = username
            await self.send(writer, "OK logged in. Type messages. /quit to exit.")
            await self.broadcast(f"[server] {username} joined.", skip=writer)

            while True:
                data = await reader.readline()
                if not data:
                    break
                msg = data.decode("utf-8").rstrip()
                if not msg:
                    continue
                if msg == "/quit":
                    break
                await self.broadcast(f"{username}: {msg}")
        except Exception:
            pass
        finally:
            if writer in self.clients:
                self.clients.discard(writer)
                self.user_by_writer.pop(writer, None)
                if username:
                    await self.broadcast(f"[server] {username} left.")
            try:
                writer.close()
                await writer.wait_closed()
            except Exception:
                pass
            # print disconnect for debug
            # print(f"[server] disconnect {addr}")

async def main():
    server = ChatServer()
    srv = await asyncio.start_server(server.handle_client, HOST, PORT)
    print(f"[server] Listening on {HOST}:{PORT}")
    async with srv:
        await srv.serve_forever()

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("\n[server] Stopped.")
