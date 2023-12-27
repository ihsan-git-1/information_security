
def choose_client_type(clientSocket):
    
    choice = input("Do you want student(1) or teacher(2): ")

    if choice == "1":
        print(b'Hello')

    elif choice == "2":
        print("Hi Teacher!")

    else:
        exit()
