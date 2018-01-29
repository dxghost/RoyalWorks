import socket
import sys

try:
    s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
except socket.error:
    print('Failed to connect')
    sys.exit()
print('Socket Created')

remote_ip=''
port=



s.connect((remote_ip,port))
message=""


try:
    s.sendall(message.enode())
except socket.error:
    print('Did not send')

print('message sent ')

reply=s.recv(4096)
print(reply.decode())
s.close()