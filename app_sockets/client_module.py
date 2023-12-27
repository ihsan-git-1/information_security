import json
import socket
import struct
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

def client_send_json_message(fields):    
    global client_socket
    # Convert the fields to a JSON string
    message = json.dumps(fields)

    # Prefix the message with its length
    message_length = len(message)
    length_prefix = struct.pack('!I', message_length)
    message_with_length = length_prefix + message.encode('utf-8')

    # Send the message to the server
    client_socket.sendall(message_with_length)

    # Wait for the server to respond
    client_receive_response()


def client_receive_response():
    length_prefix = client_socket.recv(4)
    if not length_prefix:
        return None

    # Unpack the length prefix to get the message length
    message_length = struct.unpack('!I', length_prefix)[0]

    # Receive the message with the calculated length
    message = client_socket.recv(message_length).decode('utf-8')
    
    print('********* Server ********* \n')
    print(message)
    print('********* Server ********* \n')
       

def client_close_connection():
    global client_socket
    # Close the connection
    client_socket.close()
