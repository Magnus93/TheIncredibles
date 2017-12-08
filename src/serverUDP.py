import SocketServer
#import socket
import sys
import pickle
from collections import defaultdict 
from player import * 

class serverUDP(SocketServer.BaseRequestHandler):

    #Adapted from source: https://docs.python.org/2/library/socketserver.html
    """
    This class works similarly to the TCP handler class, except that
    self.request consists of a pair of data and client socket, and since
    there is no connection the client address must be given explicitly
    when sending data back via sendto().
    """

    # handle(self): keeps the connection alive, adds
    def handle(self):
        data = self.request[0].strip()
        unpickled_data= pickle.loads(data)
#       print unpickled_data.player_id
        #update list of known players from any incoming data

        player_list[unpickled_data.player_id]=unpickled_data
        print "in my player list now: " + str( player_list) +"\n"
        
        socket = self.request[1]
        #print "{} wrote:".format(self.client_address[0])
        #print data

        #update list of addresses (client addresses) from any incoming connection
        address_list[self.client_address[0]]= self.client_address
        #print address_list
        
        self.remove_dead_player(player_list)
        players_pickled = pickle.dumps(player_list)

        #socket.sendto(data.upper(), self.client_address)
        #print "sending to \n"
        #print self.client_address
        #print "= "
        for k in address_list:
            #print address_list[k]
            #send all players not just data.upper
            socket.sendto(players_pickled, address_list[k])  #data.upper()

    def remove_dead_player(self, player_list):
        for key in player_list.copy().iterkeys():
            player = player_list[key]
            if (player.lives < 1):
                del player_list[key]
        return player_list

def start_server():
    global player_list, address_list
    player_list={}
    address_list={}
    #new= MyUDPHandler()
    HOST, PORT = "localhost", 8080
    server = SocketServer.UDPServer((HOST, PORT), serverUDP)
    server.serve_forever()


start_server()
#server.handle()
