#Exercise Client Session 7

import socket

#Now we will try to create a socket for communicating with the server

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

print("The Socket has been created")

PORT = 8080
IP = "192.168.1.134"

# Connecting to the server
s.connect((IP, PORT))
s.send(str.encode("Hiiiii"))
msg = s.recv(2048).decode("utf-8")
print("THE SERVER MESSAGE: ")
print(msg)
s.close()
