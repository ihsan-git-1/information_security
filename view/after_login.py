
from app_sockets.client_module import client_send_json_message


def options_after_login_view(username):

    print("Home Screen: \n")

    print("1. Edit Your Profile")
    choice = input("Enter your choice (1): ")

    if choice == '1':
        edit_view(username)
        
    else:
        print("Invalid choice. Please enter 1")
    

def edit_view(username):
    new_city = input("Enter new city: ")
    new_phone_number = input("Enter new phone number: ")

    edit_request = {
        "route": "edit",
        "parameters": {
            "username": username,
            "city": new_city,
            "phone_number": new_phone_number
        }
    }
    serverResponse = client_send_json_message(edit_request)