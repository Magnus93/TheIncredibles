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
        self.server_address = ('localhost', 8080)
    #change when logic for creating a player from user input is ready,
    #asking for id now to be able to test the connection for several players
        my_id = raw_input("What's your id?")
        self.player = player(int(my_id), (300,300), (255,0,255), "Valeria")
        self.list_of_players = {self.player.id:self.player}


    def start_client(self):
        #client_for_player = client();
        while (self.player.lives > 0):
            try:
                self.send_player()


                self.receive_players()
                #uncomment the line below to avoid an infinite loop
                #self.player.lives = self.player.lives - 1


            except KeyboardInterrupt:
                raise
        print("player is dead")
        self.send_player()
        self.sock.close()
    def send_player(self):
        data = pickle.dumps(self.player)
        self.sock.sendto(data, self.server_address)
        print >>sys.stderr, 'sent player to server'
    def receive_players(self):
        print >>sys.stderr, 'waiting to receive'
        #receive list of players from server
        data, server = self.sock.recvfrom(4096)
        unpickled_list=pickle.loads(data)
        #save current position of the player
        old_position = self.player.position
        #update the player belonging to the client with the details from server
        self.player = unpickled_list[self.player.id]
        #set the position of the updated player to the old position
        self.player.position = old_position
        #update player in the list received from server
        unpickled_list[self.player.id] = self.player
        #update the list of players of the client with the list received from the server
        self.list_of_players.update(unpickled_list)
        print >>sys.stderr, 'received "%s"' % self.list_of_players
        #print(str(unpickled_list[self.player.id].position))





client_for_player = client()
client_for_player.start_client()
