
from app_enum import UserEnum
from methods.auth import auth_view



def choose_client_type(clientSocket):
    
    choice = input("Do you want student(1) or teacher(2): ")
    clientSocket.send("Socket Test Wi Wi")
    if choice == "1":
        print("Hi Student!")
        auth_view(UserEnum.STUDENT)

    elif choice == "2":
        # add teacher function here 
        print("Hi Teacher!")
        auth_view(UserEnum.TEACHER)

    else:
        exit()
