import socket
from socket import AF_INET, SOCK_STREAM

clientSocket = socket.socket(AF_INET, SOCK_STREAM)
clientSocket.connect(('127.0.0.1', 8000))

clientSocket.sendall('Hola'.encode('utf-8'))

data = clientSocket.recv(1024)
print(data.decode())