import socket
from player import *


def makeclientsocket(port):
		clientsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		
		#clientsocket.connect((socket.gethostbyname('localhost'), port))
		#replaced the line above with: IP of socket needs to be hardcoded 
		clientsocket.connect(('130.238.55.70', port)) # do not change the IP! it links to a server where mysocket.py runs, AND it has the correct port(9666) accesible

		msg = raw_input('type anything and click enter... ')
		clientsocket.send(msg)
		#p = player(1, (300,300), (255,0,255), 'Nea') 
		#clientsocket.send(str(p.player_id))
		#clientsocket.send(str(p.position))
		#clientsocket.send(str(p.color))
		#clientsocket.send(p.name)


while True:
	makeclientsocket(8080)