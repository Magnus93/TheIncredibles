import socket
import sys
import pickle
from collections import defaultdict
from player import *
import game

#source: https://pymotw.com/2/socket/udp.html
# Create a UDP socket

start = False
class client:
    def __init__(self):
        self.num_player = 2
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.server_address = ('localhost', 8080)
        self.game_started = False
    #change when logic for creating a player from user input is ready,
    #asking for id now to be able to test the connection for several players
        self.player = None
        self.list_of_players = None
        self.local_game = game.local_game()

    def setup_player(self):
        name = raw_input("Name: ")    
        self.player = player(-1, (300,300), (255,0,255), name)
        self.list_of_players = [None]*self.num_player
        self.list_of_players[self.player.id] = self.player

    def start_client(self):
        #client_for_player = client();
        
        

        
        # Join game
        joined = False
        while(not joined):
            try:
                print "Sending player"
                self.send_player()


                self.receive_players()
                if self.player.id == -1:
                    for p in self.list_of_players:
                        if p.name == self.player.name:
                            self.player.id = p.id
                            self.player.position = p.position
                            joined = True 

                            if self.player.id == self.num_player-1:
                                self.game_started = True

                #uncomment the line below to avoid an infinite loop
                #self.player.lives = self.player.lives - 1


            except KeyboardInterrupt:
                raise
        
        # Wainting for everyone to join
        if self.game_started == False:
            while (not self.game_started):
                self.receive_players()
                if self.list_of_players[-1].name != "player"+str(self.num_player-1):
                    self.game_started = True


        # Run Game

        while True:
            print "Game starting"
            start = True
            self.send_player()
            
            self.receive_players()
            
            self.local_game.run(self.list_of_players, self.player.id)
            self.player = self.list_of_players[self.player.id]
            
            
            


        print("player is dead")
        self.send_player()
        self.sock.close()

    def send_player(self):
        self.player.update_position()
        data = pickle.dumps(self.player)
        self.sock.sendto(data, self.server_address)
        print >>sys.stderr, 'sent player to server'

    def receive_players(self):
        print >>sys.stderr, 'waiting to receive'
        #receive list of players from server
        data, server = self.sock.recvfrom(4096)
        unpickled_list=pickle.loads(data)
        print str(unpickled_list[0].position)
        #update the list of players of the client with the list received from the server
        if self.game_started == False:
            self.list_of_players = unpickled_list
        else:
            for pl in unpickled_list:
                if pl.id != self.player.id:
                    
                    self.list_of_players[pl.id] = unpickled_list[pl.id]
                    self.list_of_players[pl.id].position = unpickled_list[pl.id].position
        
        #for lp in self.list_of_players:
         #   print str(lp.position)
        #print str(list_of_players[0])+str( list_of_players[1])+str(list_of_players[2]) +str(list_of_players[3])+"\n"







client_for_player = client()
client_for_player.setup_player()
client_for_player.start_client()
