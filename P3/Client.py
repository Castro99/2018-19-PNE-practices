import socket

# SERVER IP, PORT
PORT = 8044
IP = "192.168.1.132"
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((IP, PORT))
msg = """actg
len
countT
aaa
"""

s.send(msg.encode())

info = s.recv(2048).decode('utf-8')
print(info)

s.close()