# Testing socket programming : 1 / 9 / 2018
# By cpt_9m0

import socket

CLIENT = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
HOST = 'localhost'
PORT = 9999

CLIENT.connect((HOST, PORT))

while True:
    print(CLIENT.recv(1024))
    print("Data received...")

