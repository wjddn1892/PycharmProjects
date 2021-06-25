import socket
from socket import AF_INET, SOCK_STREAM
import cv2

serverSocket = socket.socket(AF_INET, SOCK_STREAM)
serverSocket.bind(('', 9899))
serverSocket.listen(1)
# basic

client, addr = serverSocket.accept()


image = cv2.imread('2.jpg')
img_str = cv2.imencode('.jpg', image)[1].tostring()

size = str(len(img_str))
client.sendall(size.encode())

data = client.recv(2)
print(data.decode())

client.sendall(img_str)