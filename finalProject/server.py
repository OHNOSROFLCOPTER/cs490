#!usr/bin/python
"""
Server
"""

import socket
import threading
import time

TELEPHONE_SOCKET = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
TELEPHONE_SOCKET.bind(('', 11002))

CLIENT_SOCKET = socket.socket()
CLIENT_SOCKET.bind(('', 11001))

"""
Class for the server
"""
class Server(object):
    support_queue = []
    client_queue = []
    threads = []
    def __init__(self):
        support_thread = threading.Thread(target=self.get_telephone_connection)
        support_thread.start()
        self.threads.append(support_thread)

        client_thread = threading.Thread(target=self.get_client_connection)
        client_thread.start()
        self.threads.append(client_thread)

        matching_thread = threading.Thread(target=self.match_clients)
        matching_thread.start()
        self.threads.append(matching_thread)


    def get_telephone_connection(self):
        while 1:
            TELEPHONE_SOCKET.listen(2)
            (telephone_client, address) = TELEPHONE_SOCKET.accept()
            self.support_queue.append((telephone_client, address))
            print("{0} connected".format(str(address)))
            msg = "Welcome to work!" + "\r\n"
            telephone_client.send(msg.encode('ascii'))
            msg = "Waiting for connection..." + "\r\n"
            telephone_client.send(msg.encode('ascii'))

    def get_client_connection(self):
        while 1:
            CLIENT_SOCKET.listen(10)
            (client_client, address) = CLIENT_SOCKET.accept()
            self.client_queue.append((client_client, address))
            print("{0} connected".format(str(address)))
            msg = "Welcome to Tech Support!" + "\r\n"
            client_client.send(msg.encode('ascii'))
            msg = "We will be with you shortly" + "\r\n"
            client_client.send(msg.encode('ascii'))


    def match_clients(self):
        while True:
            if self.client_queue and self.support_queue:
                current_client_socket = self.client_queue.pop(0)[0]
                current_support_socket = self.support_queue.pop(0)[0]
                support_to_client = threading.Thread(
                    target=comms, args=(current_support_socket, current_client_socket))
                client_to_support = threading.Thread(
                    target=comms, args=(current_client_socket, current_support_socket))
                self.threads.append(support_to_client)
                self.threads.append(client_to_support)
                support_to_client.start()
                client_to_support.start()
            else:
                time.sleep(1)

def comms(source_socket, dest_socket):
    while 1:
        msg = source_socket.recv(4096)
        dest_socket.send(msg)

MY_SERVER = Server()
for thread in MY_SERVER.threads:
    thread.join()

