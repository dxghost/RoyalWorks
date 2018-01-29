import socket
import sys
from _thread import *



host=''
port =8888


s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)


print('Socket created')


try:
    s.bind((host,port))
except socket.error:
    print('Binding Failed')
    sys.exit()

print('socket bounded')

s.listen(3)


print('socket ready to listen')

def clientthread(connection):

    welcomemessage="welcome to the server"
    connection.send(welcomemessage.encode())

    while True:
        data = connection.recv(1024)
        reply='Ok' +'   '+ data.decode()
        if not data:
            break
        print(reply)
        #connection.sendall(data)
    connection.close()

mystr=''
while True:
    connection, addr = s.accept()
    print('connected with' + addr[0] + ':' + str(addr[1]))
    start_new_thread(clientthread,(connection,))

connection.close()
s.close()