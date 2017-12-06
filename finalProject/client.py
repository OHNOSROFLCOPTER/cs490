#!usr/bin/python 
"""
The phones
"""

import socket
import threading

class Client_Client:
    is_connected = False
    is_exit = False
    threads = []
    s = socket.socket()

    def __init__(self):
        #connect ot the socket
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        host = socket.gethostname()
        port = 11001
        self.s.connect((host, port))

        #Threads
        listen_thread = threading.Thread(target=self.get_message)
        send_thread = threading.Thread(target=self.send_message)
        listen_thread.start()
        send_thread.start()
        self.threads.append(listen_thread)
        self.threads.append(send_thread)


    def get_message(self):
        self.is_connected = True
        msg = ""
        while not self.is_exit:
            msg = self.s.recv(4096)
            msg = msg.decode('ascii')
            print(msg)
            if "Tech Support has disconnected" in msg:
                self.is_connected = False
            if "You are now connected" in msg:
                self.is_connected = True

    def send_message(self):
        while not self.is_exit:
            user_input = input()
            if "!!quit" in user_input:
                self.is_exit = True
            else:
                self.s.send(user_input.encode('ascii'))


CLIENT = Client_Client()
for thread in CLIENT.threads:
    thread.join()