import socket

HOST = "127.0.0.1"  # The server's hostname or IP address
PORT = 8888  # The port used by the server

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    try:
        s.connect((HOST, PORT))
        while True:
            command = input('Enter a command or use the "help" command to see the available options: ').encode('utf8')
            s.sendall(command)
            # Receiving responses from the server
            response_data = s.recv(1024).decode('utf8')
            print(response_data)

            # Exit condition
            if command.lower() == b'quit' or command.lower() == b'exit':
                print('Exiting...')
                break

    except Exception as e:
        print('Error: ', e)

