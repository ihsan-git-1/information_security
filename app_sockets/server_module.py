import asyncio
import cryptography
import datetime
import os
import struct
import socket
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography import x509
from app_router.app_router import handle_AppRouting
from ca_module import ca_cert_generator

# Global variable to store the server socket instance
server_socket = None

if not os.path.exists('/ca_module/ca-certificate.pem'):
    ca_cert_generator.generate_ca_certificate()


async def handle_client(reader, writer):
    address = writer.get_extra_info('peername')
    print(f"Connection from {address}")

    # receive request from the client
    while True:

        # Receive the length prefix
        length_prefix = await reader.readexactly(4)
        if not length_prefix:
            break  # Break the loop if no more data is received

        # Unpack the length prefix to get the message length
        message_length = struct.unpack('!I', length_prefix)[0]

        # Receive the message with the calculated length
        data = await reader.readexactly(message_length)
        message = data.decode('utf-8')

        print("Message received in server " + message)

        # Trigger the function to process the data
        data_router_response = handle_AppRouting(message)

        print("Send: " + data_router_response)

        writer.write(data_router_response.encode('utf-8'))

        await writer.drain()


async def start_socket_server(host, port):
    global server_socket
    # Create a socket object
    server_socket = await asyncio.start_server(
        handle_client, host, port)

    address = server_socket.sockets[0].getsockname()
    print(f'Server listening on {address}')

    async with server_socket:
        await server_socket.serve_forever()
