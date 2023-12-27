import json
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

    #convert the message to json
    string_json = json.dumps(message)

    # Send a message to the server
    client_socket.sendall(string_json.encode('utf-8'))

    # wait for the server to respond
    client_receive_response()


def client_receive_response():
    # Receive and print the response from the server
    response = client_socket.recv(1024)
    print('********* Server response:', response.decode('utf-8'))
       

def client_close_connection():
    global client_socket
    # Close the connection
    client_socket.close()
