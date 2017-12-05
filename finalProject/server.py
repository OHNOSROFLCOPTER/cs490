#!usr/bin/python
"""
Server
"""

import socket
import threading

TELEPHONE_SOCKET = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
TELEPHONE_SOCKET.bind(('', 11002))

CLIENT_SOCKET = socket.socket()
CLIENT_SOCKET.bind(('', 11001))

class Server(object):
    telephoneConnections = []
    threads = []
    def __init__(self):
        thread1 = threading.Thread(target=self.getTelephoneConnection)
        thread1.start()


    def getTelephoneConnection(self):
        while 1:
            TELEPHONE_SOCKET.listen(2)
            (telephoneClient, address) = TELEPHONE_SOCKET.accept()
            self.telephoneConnections.append((telephoneClient, address))
            print("{0} connected".format(str(address)))
            MSG = "Welcome to work!" + "\r\n"
            telephoneClient.send(MSG.encode('ascii'))

MY_SERVER = Server()
