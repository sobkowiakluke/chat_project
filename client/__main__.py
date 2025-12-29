from control_client import ControlClient

def main():
    client = ControlClient(server_host='127.0.0.1', server_port=5566)
    print("Starting client...")
    client.start()

if __name__ == "__main__":
    main()
