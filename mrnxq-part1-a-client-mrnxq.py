import socket


def client_socket():
    # as both code is running on same pc
    HOST = socket.gethostbyname('192.168.1.119')
    PORT = 6000  # socket server port number

    soc = socket.socket()  # instantiate
    soc.connect((HOST, PORT))  # connect to the server

    msg = input("Enter Input -> \n")  # take input
    while True:
        if msg == "Bye from client Mounika":
            soc.send(msg.encode())
            data = soc.recv(1024).decode()
            print(data)
            if(data == "Bye from server mounika"):
                break
            else:
                msg = input("Take another input \n")
        elif msg == "Hello from client Mounika":
            soc.send(msg.encode())
            data = soc.recv(1024).decode()
            print(data)
            msg = input("Take another input \n")
        else:
            soc.send(msg.encode())
            data = soc.recv(1024).decode()
            print(data)
            msg = input("Enter message \n")

    soc.close()  # close the connection


if __name__ == '__main__':
    client_socket()
