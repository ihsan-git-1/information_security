
from app_enum import UserEnum
from app_sockets.client_module import client_send_json_message
from encryptions.aes_encryption import AesEncryption
from encryptions.teacher_cert_generator import CSRGenerator
from utils import convert_string_to_key


def options_after_teacher_login_view(username):

    print("Home Screen: \n")

    print("1. Edit Your Profile")
    print("2. Verify Your Account")
    choice = input("Enter your choice (1/2): ")

    if choice == '1':
        edit_view(username)
    elif choice == '2':
        verify_teacher(username)
        
    else:
        print("Invalid choice. Please enter 1")

def verify_teacher(username):
    
   csr_generator = CSRGenerator()
   print(csr_generator.generate_csr())

 

def edit_view(username):
    new_city = input("Enter new city: ")
    new_phone_number = input("Enter new phone number: ")

    aes = AesEncryption(convert_string_to_key(username))
    city_encrypted = aes.encrypt(new_city)
    phone_encrypted = aes.encrypt(new_phone_number)

    edit_request = {
        "route": "edit",
        "parameters": {
            "username": username,
            "city": city_encrypted.decode(),
            "phone_number": phone_encrypted.decode()
        }
    }
    print("city"+ str(city_encrypted))
    print("phone_number"+ str(phone_encrypted))

    serverResponse = client_send_json_message(edit_request)


