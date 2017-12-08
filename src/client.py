import socket
import sys
import pickle
from collections import defaultdict 
from player import * 

#source: https://pymotw.com/2/socket/udp.html
# Create a UDP socket
class client:
    def __init__(self):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.server_address = ('localhost', 10000)
    #change when logic for creating a player from user input is ready
        self.player = player(1, (300,300), (255,0,255), "Valeria")
        self.list_of_players = {}

    def start_client(self):
        #client_for_player = client();
        while (self.player.lives > 0):
            try:
                self.send_player()
                self.recieve_player()
            except KeyboardInterrupt:
                raise
    def send_player(self):
        data = pickle.dumps(self.player)
        self.sock.sendto(data, self.server_address)
        print >>sys.stderr, 'sent player to server'
    def recieve_player(self):
        print >>sys.stderr, 'waiting to receive'
        data, server = self.sock.recvfrom(4096)
        unpickled_playr=pickle.loads(data)
        print >>sys.stderr, 'received "%s"' % unpickled_playr.name



#message = 'This is the message.  It will be repeated.'

client_for_player = client()
client_for_player.start_client()
