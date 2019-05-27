import socket


PORT = 8081
IP = "192.168.1.132"
MAX_OPEN_REQUESTS = 5


number_con = 0


serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
try:
    serversocket.bind((IP, PORT))

    serversocket.listen(MAX_OPEN_REQUESTS)

    while True:

        print("Waiting for connections at {}, {} ".format(IP, PORT))
        (clientsocket, address) = serversocket.accept()


        number_con += 1


        print("CONNECTION: {}. From the IP: {}".format(number_con, address))


        msg = clientsocket.recv(2048).decode("utf-8")
        print("Message from client: {}".format(msg))


        message = "Hello there, from teacher's server"
        send_bytes = str.encode(message)

        clientsocket.send(send_bytes)
        clientsocket.close()

except socket.error:
        print("ERROR problems with the port {}. Do you have permission or you are a fekas?".format(PORT))

except KeyboardInterrupt:
        print("The user just broke the server or decide to stop it")
serversocket.close()