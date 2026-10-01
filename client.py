import socket

CLIENT_NAME = "Client of Enrico Balingit"
SERVER_HOST = "localhost"
SERVER_PORT = 5300

client_socket = None

print(CLIENT_NAME)

try:
    client_number = int(input("Enter an integer between 1 and 100: "))    
except ValueError:
    print("Not an integer. Try again.")
        
try:
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((SERVER_HOST, SERVER_PORT))
    print("Connected.")
    
    message = CLIENT_NAME + ", " + str(client_number)
    print(f"Sending: {message}")
    client_socket.send(message.encode())
    
    print("Waiting for reply...")
    reply = client_socket.recv(1024).decode()
    print(f"Received: {reply}")
    
    server_name, server_num_str = reply.split(",")
    server_number = int(server_num_str)
    
    print("Client name:", CLIENT_NAME)
    print("Server name:", server_name)
    print("Client number:", client_number)
    print("Server number:", server_number)
    print("Sum:", client_number + server_number)
    
except ConnectionRefusedError:
    print("Could not connect - is the server running?")
except socket.error as e:
    print("Socket error:", e)
except ValueError as e:
    print("Bad data from server:", e)
except Exception as e:
    print("Unexpected error:", e)
finally:
    if client_socket is not None:
        client_socket.close()
        print("Socket closed. Client terminating.")
 
    