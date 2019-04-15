#Exercise Client lesson P3

    import socket

    port = 8080
    IP = "192.168.1.134"

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((IP, port))
    msg = """
    """

    s.send(msg.encode())

    message = s.recv(2048).decode('utf-8')
    print(message)

    s.close()