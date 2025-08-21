import socket

HOST = "127.0.0.1"
PORT = 8888

def main():
    with socket.create_connection((HOST, PORT), timeout=5) as s:
        r = s.makefile("r", encoding="utf-8", newline="\n")
        w = s.makefile("w", encoding="utf-8", newline="\n")
        print(f"Connected to {HOST}:{PORT}. Type and press Enter (exit/quit to leave).")
        while True:
            try:
                msg = input("> ")
            except (EOFError, KeyboardInterrupt):
                print("\nExiting...")
                break

            if msg.strip().lower() in {"exit", "quit"}:
                print("Close connection...")
                break

            w.write(msg + "\n")
            w.flush()

            reply = r.readline()
            if not reply:
                print("Connection closed by server.")
                break
            print("Answer:", reply.rstrip("\n"))

if __name__ == "__main__":
    main()
