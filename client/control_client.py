import socket

class ControlClient:
    def __init__(self, server_host='127.0.0.1', server_port=5566):
        self.server_host = server_host
        self.server_port = server_port

    def start(self):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            try:
                s.connect((self.server_host, self.server_port))
                print(f"Connected to server {self.server_host}:{self.server_port}")
                while True:
                    msg = input("Message to send (type 'exit' to quit): ")
                    if msg.lower() == 'exit':
                        break
                    s.sendall(msg.encode())
                    data = s.recv(1024)
                    print(f"Received: {data.decode()}")
            except ConnectionRefusedError:
                print(f"Cannot connect to server {self.server_host}:{self.server_port}")
