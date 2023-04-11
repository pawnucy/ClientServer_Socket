import socket

HOST = "127.0.0.1"  # The server's hostname or IP address
PORT = 8888  # The port used by the server

COMMANDS = {
    b'help': b'There will be help commands.',
    b'info': b'There will be information.',
}

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen(5)
    print(f"Server listening on {HOST}:{PORT}...")
    conn, addr = s.accept()
    print(f"Connected to client at {addr}")
    with conn:
        while True:
            data = conn.recv(1024)
            if not data:
                break
            command = data.decode('utf8').strip().lower().encode('utf8')
            response = COMMANDS.get(command, b'Unknown command')
            conn.sendall(response)
