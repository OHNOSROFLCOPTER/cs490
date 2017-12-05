#!usr/bin/python
"""
The phones
"""

import socket

S = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
S.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

HOST = socket.gethostname()
PORT = 11002

S.connect((HOST, PORT))

MSG = S.recv(4096)

S.close()
print(MSG.decode('ascii'))
