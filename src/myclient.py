import socket
from player import * 
import pickle

def makeclientsocket(port):
		clientsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		
		#For demo: IP of socket needs to be hardcoded (1. remove comment on this line and 2. comment out the next line for demo-ing)
		#use port 9666 for demo! change port number also in mysocket when demo-ing
		#clientsocket.connect(('130.238.55.70', port))

		clientsocket.connect(('104.196.165.56', port))
		#clientsocket.connect((socket.gethostbyname('localhost'), port))
		
		msg = raw_input('type anything and click enter... ')
		#clientsocket.send(msg)

		p = player(player_id=1, position=(300,300), color=(255,0,255), name='Nea') 
		pl=pickle.dumps(p)
		clientsocket.send(pl)


while True:
	makeclientsocket(9666)
