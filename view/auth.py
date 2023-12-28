
import json
from app_enum import UserEnum
from app_sockets.client_module import client_send_json_message
from view.after_login import options_after_login_view
from view.after_teacher_login import options_after_teacher_login_view

def auth_view(userType):


    print("1. Add User")
    print("2. Login")
    choice = input("Enter your choice (1/2): ")

    if choice == '1':
        sign_up_view(userType)

    elif choice == '2':
        login_view(userType)
        
    else:
        print("Invalid choice. Please enter 1, 2")

def sign_up_view(userType):

    print("Add "+userType.name+ ":")
    username = input("Enter username: ")
    city = input("Enter city: ")
    phone_number = input("Enter phone number: ")
    password = input("Enter password: ")

    # Send a "sign up" request
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


def login_view(userType):
    print("Login \n")
    username = input("Enter username: ")
    password = input("Enter password: ")
    # Send a "login" request
    login_request = {
        "route": "login",
        "parameters": {
            "username": username,
            "password": password
        }
    }
    serverResponse = client_send_json_message(login_request)
    
    if(serverResponse == "Login failed no account available"):
        return
    else:
     if(userType is UserEnum.STUDENT):options_after_login_view(username)
     elif(userType is UserEnum.TEACHER):options_after_teacher_login_view(username)

 