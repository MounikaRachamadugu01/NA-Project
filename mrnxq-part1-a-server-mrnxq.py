import socket


def server_socket():
    # get the hostname
    HOST = ''
    PORT = 6000  # initiate port no above 1024

    sock = socket.socket()  # get instance
    # look closely. The bind() function takes tuple as argument
    sock.bind((HOST, PORT))  # bind host address and port together
    sock.listen(1)
    conn, addr = sock.accept()  # accept new connection
    print("Got a new connection from: " + str(addr))
    while True:
        # receive data stream. it won't accept data packet greater than 1024 bytes
        data = conn.recv(1024).decode()
        if data == "Bye from client Mounika":
            print(data)
            conn.send(str.encode("Bye from server Mounika"))
            break
        elif data == "Hello from client Mounika":
            print(data)
            conn.send(str.encode("Hello from server Mounika"))
        else:
            print(data)
            conn.send(data.encode())  # send data to the client
    conn.close()  # close the connection


if __name__ == '__main__':
    server_socket()
