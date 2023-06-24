import socket

def start_server():
    host = 'localhost'  # Host IP address
    port = 8080  # Port to listen on

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen(1)
    print("Server listening on {}:{}".format(host, port))

    client_socket, address = server_socket.accept()
    print("Client connected from {}".format(address[0]))

    while True:
        command = input("Enter command: ")

        if command.lower() == 'exit':
            break

        # Send command to client
        client_socket.sendall(command.encode())

        # Receive output from client
        output = client_socket.recv(4096).decode()
        print("Output:\n{}".format(output))

    # Send exit command to client
    client_socket.sendall("exit".encode())

    # Close the connection
    client_socket.close()
    server_socket.close()

if __name__ == '__main__':
    start_server()
