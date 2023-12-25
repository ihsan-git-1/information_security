
import os
import socket
import threading
from flask import Flask as FlaskAuth
from pathlib import Path
from sqlalchemy.ext.declarative import declarative_base
from dotenv import load_dotenv
from sqlalchemy import MetaData, create_engine

from accounts.methods.choose_user_type import choose_client_type

BASE_DIR = Path(__file__).resolve().parent.parent

load_dotenv(os.path.join(BASE_DIR, ".env"))

MEDIA_ROOT = os.path.join(BASE_DIR, "accounts", "static", "assets")

UPLOAD_FOLDER = os.path.join(MEDIA_ROOT, "profile")

metadata = MetaData()

host = "127.0.0.1"
port = 12345

choice = input("Do you want server(1) or client(2): ")

if choice == "1":
    # Create a socket server
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((host, port))

    # Listen for connections
    server.listen(10)

    print(f"Server listening on {host}:{port}")
    client, _ = server.accept()

elif choice == "2":
    clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    clientSocket = clientSocket.connect((host, port))

    choose_client_type(clientSocket)

else:
    exit()




