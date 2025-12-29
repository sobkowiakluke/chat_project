from control_server import ControlServer

def main():
    server = ControlServer(host='0.0.0.0', port=5566)
    print("Starting server on port 5566...")
    server.start()

if __name__ == "__main__":
    main()
