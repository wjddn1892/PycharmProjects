import socket
import numpy as np
from socket import AF_INET, SOCK_STREAM
import cv2

client = socket.socket(AF_INET, SOCK_STREAM)
client.connect(('localhost', 9899))  # tuple


data = client.recv(1024)


size = int(data.decode()) #decode는 스트링에서 바이트
print("image size")
print(size)

client.sendall("ok".encode())

image_data = b''
while size > 0:
    print(size)
    image_data += client.recv(1024)
    size -= 1024

nparr = np.fromstring(image_data, np.uint8)
image = cv2.imdecode(nparr, cv2.IMREAD_COLOR)

cv2.imwrite('image.jpeg', image)