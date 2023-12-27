

def receiving_messages(c):
    while True:
        ##print("TEst: " + c.recv(1024).decode())
        data = c.recv(1024)
        if not data:
            print("No Data")
        else:
            print('Received message:', data.decode('utf-8'))
 

