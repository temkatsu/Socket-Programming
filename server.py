import socket
import random

SERVER_NAME = "Server of Eliana Morin"
SERVER_PORT = 5300

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    server_socket.bind(("", SERVER_PORT))
    server_socket.listen(1)

    print(SERVER_NAME)
    print("Server is waiting for a client...")

    while True:

        try:
            connection_socket, client_address = server_socket.accept()
            print("Client connected.")

            try:
                message = connection_socket.recv(1024).decode()

                if not message:
                    print("Client sent no data.")
                    connection_socket.close()
                    continue

                print(f"Received: {message}")

                parts = message.split(",")

                if len(parts) != 2:
                    print("Invalid message format.")
                    connection_socket.close()
                    continue

                client_name = parts[0].strip()

                try:
                    client_number = int(parts[1].strip())
                except ValueError:
                    print("Client number is not an integer.")
                    connection_socket.close()
                    continue

                # Check if client number is between 1 and 100
                if client_number < 1 or client_number > 100:
                    print("Client number must be between 1 and 100.")
                    connection_socket.close()
                    break

                print("Client name:", client_name)
                print("Server name:", SERVER_NAME)

                server_number = random.randint(1, 100)

                total = client_number + server_number

                print("Client number:", client_number)
                print("Server number:", server_number)
                print("Sum:", total)

                # Send server name and server number to client
                response = SERVER_NAME + ", " + str(server_number)
                print(f"Sending: {response}")

                connection_socket.send(response.encode())

            except UnicodeDecodeError:
                print("Could not decode the message from the client.")

            except socket.error as e:
                print("Socket error:", e)

            finally:
                connection_socket.close()
                print("Connection Socket Closed")
                print()

        except socket.error as e:
            print("Error accepting connection:", e)

except OSError as e:
    print("Could not start server:", e)

finally:
    server_socket.close()
    print("Server terminated.")
