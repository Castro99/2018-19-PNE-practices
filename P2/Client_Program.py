#Exercise II lesson P2
import socket
from Ex_1 import Seq

while True:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    print("Socket has been created")

    PORT = 8080
    IP = "192.168.1.38"


    file = input("Type a message: ")
    seq = Seq(file)
    rev = Seq.reversed(seq)
    comp = Seq.complement(rev)
    comp1 = comp.strbases

    s.connect((IP ,PORT))

    s.send(str.encode(comp1))

    msg = s.recv(2048).decode('utf-8')

s.close()