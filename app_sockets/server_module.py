import asyncio

# Global variable to store the server socket instance
server_socket = None

async def handle_client(reader, writer):
    address = writer.get_extra_info('peername')
    print(f"Connection from {address}")

    data = await reader.read(100)
    message = data.decode('utf-8')
    print(f"Received message: {message}")

    print("Send: Message received!")
    writer.write("Message received!".encode('utf-8'))
    await writer.drain()

    print("Closing the connection")
    writer.close()

async def start_socket_server(host, port):
    global server_socket
    # Create a socket object
    server_socket = await asyncio.start_server(
        handle_client, host, port)

    addr = server_socket.sockets[0].getsockname()
    print(f'Server listening on {addr}')

    async with server_socket:
        await server_socket.serve_forever()

