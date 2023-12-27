import asyncio
import struct
from app_router.app_router import handle_AppRouting

# Global variable to store the server socket instance
server_socket = None

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

        print("Message Recived in server " + message)

        # Trigger the function to process the data
        dataRouterResponse = handle_AppRouting(message)

        print("Send: " + dataRouterResponse)

        writer.write(dataRouterResponse.encode('utf-8'))

        await writer.drain()

async def start_socket_server(host, port):
    global server_socket
    # Create a socket object
    server_socket = await asyncio.start_server(
        handle_client, host, port)

    addr = server_socket.sockets[0].getsockname()
    print(f'Server listening on {addr}')

    async with server_socket:
        await server_socket.serve_forever()

