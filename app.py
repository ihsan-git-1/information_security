
import socket
import threading
from database.database import initalizeDataBaseTables

from methods.choose_user_type import choose_client_type
from methods.server_handling import receiving_messages


host = "127.0.0.1"
port = 5001

initalizeDataBaseTables()

choice = input("Do you want server(1) or client(2): ")

if choice == "1":
    # Create the socket of the server
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((host, port))

    # Listen for connections
    server.listen()

    print(f"Server listening on {host}:{port}")
    client, _ = server.accept()

    threading.Thread(target=receiving_messages, args=(client,)).start()

elif choice == "2":

    # Note : uncomment the input in the day of the presentation .

    # ipInput = input("Enter IP address: \n")
    # portInput = input("Enter port: \n")

    clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    clientSocket = clientSocket.connect((host, int(port)))

    # client threads to start here :

    # choose client type thread
    threading.Thread(target=choose_client_type, args=(clientSocket,)).start()

else:
    exit()




