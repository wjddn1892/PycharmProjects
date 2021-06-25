import socket
from socket import AF_INET, SOCK_STREAM

serverSocket = socket.socket(AF_INET, SOCK_STREAM)
serverSocket.bind(('', 8000))

serverSocket.listen(1)

clientSocket, addr = serverSocket.accept()

data = clientSocket.recv(1024)

print(data.decode())

clientSocket.sendall('Good'.encode())
