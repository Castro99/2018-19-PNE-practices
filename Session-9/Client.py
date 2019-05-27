#Exercise Client Session 9

import socket

IP = "192.168.1.132"
PORT = 8080

while True:
    # Client blocking the server
    msg = input(">")

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # establishing connection to the Server
    s.connect((IP, PORT))

    # Sending request message to the server
    s.send(str.encode(msg))

    # Receive servers response
    response = s.recv(2048).decode()

    # Print response
    print("Response: {}".format(response))

    s.close()