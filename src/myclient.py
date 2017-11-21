import socket
from player import *


def makeclientsocket(port):
		clientsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		clientsocket.connect(('nl119-155-116.student.uu.se', port))
		msg = raw_input('type anything and click enter... ')
		clientsocket.send(msg)
		#p = player(1, (300,300), (255,0,255), 'Nea') 
		#clientsocket.send(str(p.player_id))
		#clientsocket.send(str(p.position))
		#clientsocket.send(str(p.color))
		#clientsocket.send(p.name)


#while True:
makeclientsocket(8080)