import socket
import sys
import pickle
from collections import defaultdict
import player
import game_client
import packet

#source: https://pymotw.com/2/socket/udp.html
# Create a UDP socket


start = False
class client:
    def __init__(self):
        self.num_players = None
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.server_address = ('localhost', 8080)
        self.game_started = False
    #change when logic for creating a player from user input is ready,
    #asking for id now to be able to test the connection for several players
        self.player_id = None
        self.list_of_players = None
        self.local_game = game_client.local_game()

    def setup_player(self):
        name = raw_input("Name: ")
        request_pack = packet.join_request(name)
        self.send_packet(request_pack)
        print "Waiting to join game..."
        answer_packet = self.receive_packet()
        if answer_packet.get_type() == "join_reply":
            data = answer_packet.get_data()
            if data["answer"]:
                print "Congrats "+ name +" you are in the game."
                print "Your ID: \t"+ str(data["id"])
                print "Your Color: \t"+ str(data["color"])
                print "Your Pos: \t"+ str(data["position"])
                print "# of players\t"+str(data["num_players"])
                me_player = player.player(data["id"], data["position"], data["color"], name)
                self.num_players = data["num_players"]
                self.list_of_players = [None]*self.num_players
                self.list_of_players[data["id"]] = me_player
                self.player_id = data["id"]
                return True
            else:
                print "The game is full. Better luck next time."
                return False

    def start_client(self):
        #client_for_player = client();
        print "Client started"

        print "Waiting for others players to join..."
        in_lobby = True
        while(in_lobby):
            pack = self.receive_packet()
            if pack.get_type() == "initial_other_player":
                data = pack.get_data()
                print "\nreceived new player:"+str(data["color"]) + str(data["id"]) + str(data["name"])
                playr = player.player(data["id"], data["position"], data["color"], data["name"])
                playr.angle = data["angle"]
                self.list_of_players[data["id"]] = playr
            elif pack.get_type() == "starting_game":
                in_lobby = False

        self.local_game.start_game()
        print "local game started"
        in_game = True
        while(in_game):
            self.local_game.run(self.list_of_players, self.player_id)

        #self.send_player()
        self.sock.close()
        print "sock closed"

    def send_packet(self, pack):
        pickle_pack = pickle.dumps(pack)
        self.sock.sendto(pickle_pack, self.server_address)

    def receive_packet(self):
        pickle_pack, server = self.sock.recvfrom(4096)
        pack = pickle.loads(pickle_pack)
        print pack
        return pack

    def send_player(self):
        data = pickle.dumps(self.player)
        self.sock.sendto(data, self.server_address)

    def receive_players(self):
        #print >>sys.stderr, 'waiting to receive'
        #receive list of players from server
        data, server = self.sock.recvfrom(4096)
        unpickled_list=pickle.loads(data)
        #print str(unpickled_list[1].position) + str( unpickled_list[1].name)
        #update the list of players of the client with the list received from the server
        if self.game_started == False:
            self.list_of_players = unpickled_list
        else:
            for pl in unpickled_list:
                if pl.id != self.player.id:

                    self.list_of_players[pl.id] = unpickled_list[pl.id]
                    print str(self.list_of_players[pl.id].angle)
                    #if not self.immortal:
                     #   self.list_of_players[pl.id].lives = unpickled_list[pl.id].lives
                if not unpickled_list[pl.id].immortal:
                    self.list_of_players[pl.id].lives = unpickled_list[pl.id].lives


if __name__ == '__main__':
    client_for_player = client()

    if client_for_player.setup_player():
        print "Accepted into game!"
        client_for_player.start_client()
    else:
        pass
    print "Bye"
