
import socket

from methods.choose_user_type import choose_client_type


host = "127.0.0.1"
port = 12345

choice = input("Do you want server(1) or client(2): ")

if choice == "1":
    # Create the socket of the server
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((host, port))

    # Listen for connections
    server.listen(10)

    print(f"Server listening on {host}:{port}")
    client, _ = server.accept()

elif choice == "2":
    clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    clientSocket = clientSocket.connect((host, port))

    # choose client type 
    choose_client_type(clientSocket)

else:
    exit()




