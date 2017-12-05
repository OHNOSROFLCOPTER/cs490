#!usr/bin/python
"""
This is client
"""

import socket

S = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
HOST = socket.gethostname()

PORT = 9999

S.connect((HOST, PORT))

MSG = S.recv(4096)

S.close()
print(MSG.decode('ascii'))
