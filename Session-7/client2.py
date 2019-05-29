import socket

# Now we will try to create a socket for communicating with the server

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

print("The Socket has been created")

PORT = 8080
IP = "212.128.253.102"
#conncet to the server
s.connect((IP, PORT))

while True:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((IP, PORT))
    s.send(str.encode(input('message: ')))
    s.close()

msg = s.recv(2048).decode('utf-8')
print(msg)

s.close()

print('the end')