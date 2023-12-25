
import os
import socket
import threading
from flask import Flask as FlaskAuth
from pathlib import Path
from sqlalchemy.ext.declarative import declarative_base
from dotenv import load_dotenv
from sqlalchemy import create_engine

BASE_DIR = Path(__file__).resolve().parent.parent

load_dotenv(os.path.join(BASE_DIR, ".env"))

MEDIA_ROOT = os.path.join(BASE_DIR, "accounts", "static", "assets")

UPLOAD_FOLDER = os.path.join(MEDIA_ROOT, "profile")

DataBaseDeclare = declarative_base()

def create_app():

    # Create a base class for declarative class definitions
    DATABASE_URL = os.getenv('DATABASE_URI', None)
    engine = create_engine(DATABASE_URL, echo=True)
    DataBaseDeclare.metadata.create_all(engine)

    choose_client_or_server()

def choose_client_or_server():
    host = "127.0.0.1"
    port = 12345
    choice = input("Do you want server(1) or client(2): ")
    if choice == "1":
        # Create a socket server
        server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server.bind((host, port))
        server.listen()
        print(f"Server listening on {host}:{port}")
        serverApp, _ = server.accept()

    elif choice == "2":
        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        clientSocket = client.connect((host, port))
    else:
        exit()

    threading.Thread(target=choose_client_type, args=(clientSocket,)).start()  


def choose_client_type(clientSocket):
    choice = input("Do you want student(1) or teacher(2): ")

    if choice == "1":
        clientSocket.sendall("Hi Student!")

    elif choice == "2":
        clientSocket.sendall("Hi Teacher!")

    else:
        exit()
