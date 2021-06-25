import socket
from socket import AF_INET, SOCK_STREAM

clientSocket = socket.socket(AF_INET, SOCK_STREAM)
clientSocket.connect(('127.0.0.1', 8000))


while True:
    recvData = clientSocket.recv(1024)
    print('상대방 : ', recvData.decode('utf-8'))

    sendData = input('>>>')
    clientSocket.sendall(sendData.encode('utf-8'))