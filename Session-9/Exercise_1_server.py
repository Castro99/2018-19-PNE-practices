#Exercise I lesson 9

import socket
import termcolor

PORT = 8081
IP = "192.168.1.134"

MAX_OPEN_REQUEST = 5


def process_client(cs):

    msg = cs.recv(2048).decode("utf-8")
    if msg == "Exit":
        cs.send(str.encode(" The server has finished"))

        cs.close()
        return False
    msg_print = termcolor.colored(msg, 'green')
    print("Message from the client: {}".format(msg_print))

    msg_send = termcolor.colored(msg, 'grey')
    cs.send(str.encode(msg_send))

    cs.close()
    return True


serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

serversocket.bind((IP, PORT))

serversocket.listen(MAX_OPEN_REQUEST)

print("Socket ready: {}".format(serversocket))
active = True
while active:

    print("Waiting for connection at: {}, {}".format(IP, PORT))
    (clientsocket, address) = serversocket.accept()

    if process_client(clientsocket):


        print("Attending client: {}".format(address))
    else:
        active = False