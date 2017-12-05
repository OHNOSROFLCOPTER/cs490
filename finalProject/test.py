#!usr/bin/python
"""
A simple server
"""

import socket

SERVERSOCKET = socket.socket(
    socket.AF_INET, socket.SOCK_STREAM)

SERVERSOCKET.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

HOST = socket.gethostname()
PORT = 9999

SERVERSOCKET.bind((HOST, PORT))

SERVERSOCKET.listen(15)

while True:
    CLIENTSOCKET, ADDR = SERVERSOCKET.accept()
    print("Connection from {0}".format(str(ADDR)))
    MSG = "Thank you for connecting" + "\r\n"
    CLIENTSOCKET.send(MSG.encode('ascii'))
    CLIENTSOCKET.close()
