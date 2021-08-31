import socket

class Netcat(object):

    def __init__(self):
        self.address = (socket.gethostname(), 1234)
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def connect(self):

        self.socket.connect(self.address)

    def read(self, length=1024):
        return self.socket.recv(length)

    def write(self, data):
        self.socket.send(data.encode('utf-8'))

    def close(self):
        self.socket.close()


