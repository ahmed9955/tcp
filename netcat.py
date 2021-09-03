import socket

class Netcat(object):


    def connect(self, host, port):

        if not isinstance(host, str):
            raise Exception('Host must be ip address!')
        try:
            address = socket.getaddrinfo(host, port, proto=socket.IPPROTO_TCP)[0][4]
        except IndexError:
            raise Exception('unknown hostname or ip')

        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.connect(address)

    def read(self, length=1024):
        return self.socket.recv(length)

    def write(self, data):
        self.socket.send(data.encode('utf-8'))

    def close(self):
        self.socket.close()