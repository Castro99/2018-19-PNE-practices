# Exercise 3 Session 7

import socket

while True:

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    print("The Socket has been created")

    PORT = 8080
    #Mario IP
    IP = "212.128.253.59"


    file = input("TYPE OF MESSAGE: ")
    s.connect((IP, PORT))

    s.send(str.encode(file))

    msg = s.recv(2048).decode("utf-8")
    print("THE SERVER MESSAGE: ")
    print(msg)

    s.close()


    print("The end")