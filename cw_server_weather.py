import socket, json

HOST = "127.0.0.1"
PORT = 8888

with open("weather.json", "r", encoding="utf-8") as f:
    DATA = json.load(f)

INDEX = {city.casefold(): week for city, week in DATA.items()}

def handle(conn):
    r = conn.makefile("r", encoding="utf-8", newline="\n")
    w = conn.makefile("w", encoding="utf-8", newline="\n")
    for line in r:
        city = line.strip()
        if not city:
            continue
        week = INDEX.get(city.casefold())
        if not week:
            w.write('{"error":"not found"}\n'); w.flush(); continue
        payload = json.dumps({"city": city, "forecast": week},
                             ensure_ascii=False, separators=(",", ":"))
        w.write(payload + "\n"); w.flush()

def main():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as srv:
        srv.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        srv.bind((HOST, PORT))
        srv.listen(5)
        print(f"Listening on {HOST}:{PORT}")
        while True:
            conn, addr = srv.accept()
            print("Connected:", addr)
            try:
                handle(conn)
            finally:
                conn.close()
                print("Closed:", addr)

if __name__ == "__main__":
    main()
