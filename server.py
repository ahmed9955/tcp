import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((socket.gethostname(), 1234))
s.listen(5)

while True:
    clientsocket, address = s.accept()
    print(f"connection form {address} has been established")
    clientsocket.send(bytes("welcome to server", "utf-8"))
    data = clientsocket.recv(1024)
    print(data)
    clientsocket.close()
