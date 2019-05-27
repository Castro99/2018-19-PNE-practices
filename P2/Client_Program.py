#Exercise II lesson P2
import socket
from P2.Ex_1 import Seq



print("Socket has been created")

PORT = 8024
IP = "192.168.1.132"

#ask the user for a sequence
while True:
    #ALWAYS ASK THE USEWR FOR THE MESSAGE BEFORE SENDING IT TO THE SERVER, BECAUSE OTHERWISE YOU'RE BLOCKING THE SERVER
    seq = Seq(input('enter your sequence: '))

    reverse = seq.reverse()
    comp = seq.complement()

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((IP, PORT))
    info = '\nComplementary chain: {} \nReverse chain: {}'.format(comp, reverse)
    s.send(info.encode())