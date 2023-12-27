
from app_enum import UserEnum
from methods.auth import auth_view



def choose_client_type(clientSocket):
    
    choice = input("Do you want student(1) or teacher(2): ")

    if choice == "1":
        auth_view(UserEnum.STUDENT)
        print(b'Hello')

    elif choice == "2":
        # add teacher function here 
        auth_view(UserEnum.TEACHER)
        print("Hi Teacher!")

    else:
        exit()
