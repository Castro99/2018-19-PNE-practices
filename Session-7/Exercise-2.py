# Programming our first client Exercise 2 Session 7

import socket

while True:
    # Create a socket for communicating with the server

    s = socket.socket(socket. AF_INET, socket.SOCK_STREAM)

    print("The Socket has been created")

    PORT = 8080
    IP = "192.168.1.134"
    # Connect to server

    s.connect((IP, PORT))

    # Encode convert a string to bytes

    s.send(str.encode(input("WRITE A MESSAGE: ")))

    msg = s.recv(2048).decode("utf-8")
    print("THE SERVER MESSAGE")
    print(msg)