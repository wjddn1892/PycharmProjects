import socket

serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serverSocket.bind(('', 8000))
serverSocket.listen(1)
print('waiting for client')
clientSocket, addr = serverSocket.accept()
print('client connected')


while True:
    sendData = input('>>>')
    clientSocket.send(sendData.encode('utf-8'))

    recvData = clientSocket.recv(1024)
    print('상대방 :', recvData.decode('utf-8'))