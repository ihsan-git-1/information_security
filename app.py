
from asyncio import start_server
import asyncio
import threading
from app_sockets.client_module import connect_to_server
from app_sockets.server_module import start_socket_server
from database.database import initalizeDataBaseTables
from methods.choose_user_type import choose_client_type


host = "127.0.0.1"
port = 5001

initalizeDataBaseTables()

choice = input("Do you want server(1) or client(2): ")

def initialize_client_threads():
    #threads of the client after start 
    threading.Thread(target=choose_client_type, args=()).start()

if choice == "1":

    asyncio.run(start_socket_server(host, port))

elif choice == "2":

    connect_to_server(host, port)
    initialize_client_threads()

else:
    exit()




