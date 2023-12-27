
import json
from app_sockets.client_module import client_send_json_message
from database.database import login_user_db


def auth_view(userType):

    print("1. Add User")
    print("2. Login")
    choice = input("Enter your choice (1/2): ")

    if choice == '1':
        sign_up_view(userType)

    elif choice == '2':
        login_view()
        
    else:
        print("Invalid choice. Please enter 1, 2")

def sign_up_view(userType):

    print("Add "+userType.name+ ":")
    username = input("Enter username: ")
    city = input("Enter city: ")
    phone_number = input("Enter phone number: ")
    password = input("Enter password: ")

    # Send a "login" request
    sign_up_request = {
        "route": "signup",
        "parameters": {
            "username": username,
            "city": city,
            "phone_number": phone_number,
            "password": password,
            "user_type": userType.name
        }
    }
    client_send_json_message(sign_up_request)


def login_view():
    login_attempts = 3  # Set the maximum number of login attempts
    while login_attempts > 0:
        print("Login \n")
        username = input("Enter username: ")
        password = input("Enter password: ")
        user = login_user_db(username, password)
        if user:
            print(f"Login successful! Welcome, {user[1]}")
            break
        else:
            login_attempts -= 1
            print(f"Login failed. {login_attempts} attempts remaining.")
    else:
        print("Maximum login attempts reached. Exiting.")
            