import socket

serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serverSocket.bind(('127.0.0.1', 8000))

serverSocket.listen(1)

clientSocket, addr = serverSocket.accept()

data = clientSocket.recv(1024)

print(data.decode())

clientSocket.sendall('Good'.encode())
