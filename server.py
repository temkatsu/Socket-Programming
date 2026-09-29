import socket
import random

SERVER_NAME = "Server of Eliana Morin"
SERVER_PORT = 5000

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(("", SERVER_PORT))
server_socket.listen(1)

print(SERVER_NAME)
print("Server is waiting for a client...")

while True:

    connection_socket, client_address = server_socket.accept()
    message = connection_socket.recv(1024).decode()

    parts = message.split(",")

    client_name = parts[0]
    client_number = int(parts[1])

    # Check if client number is between 1 and 100
    if client_number < 1 or client_number > 100:
        connection_socket.close()
        break

    print("Client name:", client_name)
    print("Server name:", SERVER_NAME)

    server_number = random.randint(1, 100)

    total = client_number + server_number

    print("Client number:", client_number)
    print("Server number:", server_number)
    print("Sum:", total)
    print()

    # Send server name and server number to client
    response = SERVER_NAME + "," + str(server_number)
    connection_socket.send(response.encode())

    connection_socket.close()

server_socket.close()

print("Server terminated.")
