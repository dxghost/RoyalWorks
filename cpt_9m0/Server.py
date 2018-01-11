# Testing socket programming : 1 / 9/ 2018
# By cpt_9m0

import socket

SERVER = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
HOST = 'localhost'
PORT = 9999

SERVER.bind((HOST, PORT))
SERVER.listen(10)
data_list = [1, 2, 3, 4]

while True:
    host, port = SERVER.accept()
    print('Client connected by : ', port)
    host.send(b'123')
    print('Data sent...')
    host.close()