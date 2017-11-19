#BASIC client
#run this one after you've ran server.py
import socket

clientsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
clientsocket.connect(('localhost', 8089))
msg = raw_input('type anything and click enter... ')
clientsocket.send(msg)