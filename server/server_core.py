import socket
import threading

class ControlServer:
    def __init__(self, host='0.0.0.0', port=5566):
        self.running = True
        self.host = host
        self.port = port
        self.clients = []  # lista podłączonych klientów

    def start(self):
        """Uruchamia serwer TCP i akceptuje połączenia w pętli."""
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_socket.bind((self.host, self.port))
        self.server_socket.listen(5)
        self.server_socket.settimeout(1.0)

        print(f"Server listening on {self.host}:{self.port}")

        while self.running:
            try:
                client_socket, addr = self.server_socket.accept()
                print(f"Połączenie z adresu: {addr}")

                # dodajemy klienta do listy i startujemy wątek obsługi
                self.clients.append(client_socket)
                threading.Thread(target=self.handle_client, args=(client_socket, addr), daemon=True).start()

            except socket.timeout:
                # nic nie robimy, pozwalamy pętli sprawdzić self.running
                pass
            except OSError:
                # socket został zamknięty w stop()
                break

    def stop(self):
        """Zatrzymuje serwer i zamyka socket."""
        self.running = False
        self.server_socket.close()
        print("Server stopped.")

    def handle_client(self, client_socket, addr):
        """Obsługa pojedynczego klienta – aktualnie echo."""
        try:
            while True:
                data = client_socket.recv(1024)
                if not data:
                    break
                # echo
                client_socket.sendall(data)
        except Exception as e:
            print(f"Client {addr} error: {e}")
        finally:
            print(f"Connection closed: {addr}")
            if client_socket in self.clients:
                self.clients.remove(client_socket)
            client_socket.close()
