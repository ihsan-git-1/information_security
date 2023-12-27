import socket
import threading

# Global variable to store the client socket instance
client_socket = None

def connect_to_server(host , port):
    global client_socket
    # Create a socket object
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Connect to the server
    server_address = (host, port)
    client_socket.connect(server_address)

def client_send_message(message):
    global client_socket
    # Send a message to the server
    client_socket.sendall(message.encode('utf-8'))
    receive_response()

def receive_response():
    
    # Receive and print the response from the server
    response = client_socket.recv(1024)
    print('Received response:', response.decode('utf-8'))
       

def close_connection():
    global client_socket
    # Close the connection
    client_socket.close()
