
from app_enum import UserEnum
from methods.auth import auth_view
from app_sockets.client_module import client_send_message

def choose_client_type():
    
    choice = input("Do you want student(1) or teacher(2): ")

    if choice == "1":
        print("Hi Student!")
        auth_view(UserEnum.STUDENT)
        
    elif choice == "2":
        print("Hi Teacher!")
        auth_view(UserEnum.TEACHER)

    else:
        exit()
