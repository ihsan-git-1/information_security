from app_enum import UserEnum
from app_sockets.client_module import client_send_json_message
from encryptions.aes_encryption import AesEncryption
from encryptions.teacher_csr_generator import CSRGenerator
from utils import convert_string_to_key
from ca_module import ca_cert_generator, teacher_cert_generator


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
    print("city: " + str(city_encrypted))
    print("phone_number: " + str(phone_encrypted))

    serverResponse = client_send_json_message(edit_request)


def verify_teacher(username):
    csr_generator = CSRGenerator()
    _, teacher_csr = csr_generator.generate_csr(username)
    # Send a "verification_request" request
    verification_request = {
        "route": "verify",
        "parameters": {
            "username": username,
            "csr": teacher_csr
        }
    }
    ca_cert, ca_key = ca_cert_generator.generate_ca_certificate()

    teacher_cert_generator.generate_teacher_certificate(ca_cert, ca_key, teacher_csr, username)
    server_response = client_send_json_message(verification_request)
