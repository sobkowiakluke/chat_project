import threading
from server_core import ControlServer

def console_loop(server):
    while True:
        cmd = input().strip().lower()
        if cmd == "q":
            server.stop()
            print("Server shutdown requested")
            break

def main():
    server = ControlServer(host='0.0.0.0', port=5566)
    threading.Thread(target=server.start, daemon=True).start()
    threading.Thread(target=console_loop, args=(server,), daemon=True).start()
    print("Starting server on port 5566...")

if __name__ == "__main__":
    main()
