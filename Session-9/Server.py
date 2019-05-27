#Exercise Server Session 9

import socket

PORT = 8081
IP = "192.168.1.132"
MAX_OPEN_REQUEST = 5

# Create a socket for connecting to the clients
serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

serversocket.bind((IP, PORT))

serversocket.listen(MAX_OPEN_REQUEST)

print("Socket ready: {}".format(serversocket))

while True:

    print("Waiting for connections at {}, {}".format(IP, PORT))
    (clientsocket, address) = serversocket.accept()

    # Attending client
    print("Attending  client: {}".format(address))

    # Closing socket
    clientsocket.close()