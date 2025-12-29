import socket
import threading

class ControlServer:
    def __init__(self, host='0.0.0.0', port=5566):
        self.host = host
        self.port = port
        self.clients = []  # lista podłączonych klientów

    def start(self):
        server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server_socket.bind((self.host, self.port))
        server_socket.listen(5)
        print(f"Server listening on {self.host}:{self.port}")

        while True:
            client_socket, addr = server_socket.accept()
            print(f"New connection from {addr}")
            self.clients.append(client_socket)
            threading.Thread(target=self.handle_client, args=(client_socket, addr)).start()

    def handle_client(self, client_socket, addr):
        try:
            while True:
                data = client_socket.recv(1024)
                if not data:
                    break
                # na razie echo: odsyłamy do tego samego klienta
                client_socket.sendall(data)
        except Exception as e:
            print(f"Client {addr} error: {e}")
        finally:
            print(f"Connection closed: {addr}")
            self.clients.remove(client_socket)
            client_socket.close()
