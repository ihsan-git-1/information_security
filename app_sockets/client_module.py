import json
import socket
import struct
import threading
import ssl

# Global variable to store the client socket instance
client_socket = None


def connect_to_server(host, port, cert_path=None, key_path=None, force_secure=False):
    global client_socket
    server_address = (host, port)
    if force_secure and (not cert_path or not key_path):
        # User doesn't have a certificate and secure connection is forced
        print("Secure connection is required, but you don't have a valid certificate yet.")
        print("Please acquire a certificate and try again.")
        return  # Terminate connection attempt

    if cert_path and key_path:  # Use secure connection if certificate is available
        context = ssl.SSLContext(ssl.PROTOCOL_TLS_CLIENT)
        #context.check_hostname = False
        #context.verify_mode = ssl.CERT_NONE
        context.load_cert_chain(certfile=cert_path, keyfile=key_path)
        client_socket = context.wrap_socket(socket.socket(socket.AF_INET, socket.SOCK_STREAM),server_hostname=host)
        client_socket.connect(server_address)

    else:
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # Connect to the server
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
    return client_receive_response()


def client_receive_response():
    # Receive and print the response from the server
    response = client_socket.recv(1024)
    print('\n********* Server **********')
    print(response.decode('utf-8'))
    print('********* Server **********\n')
    return response.decode('utf-8')


def client_close_connection():
    global client_socket
    # Close the connection
    client_socket.close()