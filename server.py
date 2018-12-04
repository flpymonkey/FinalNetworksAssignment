import socket
import numpy as np
import cv2


UDP_IP = "127.0.0.1"
UDP_PORT = 5005

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind((UDP_IP, UDP_PORT))
s = ""
while True:
    data, addr = sock.recvfrom(46080)
    s += data
    if len(s) == (46080*20) and s <= 0:
        frame = np.fromstring(s, dtype='uint8')
        frame = frame.reshape(480, 640, 3)
        cv2.imshow('server_frame', frame)
        s = ""
        a = 10
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
