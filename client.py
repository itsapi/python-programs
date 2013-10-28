import socket

s = socket.socket()
host = '2.2.2.102'
port = 12347

s.connect((host, port))
print(s.recv(1024))
s.close
