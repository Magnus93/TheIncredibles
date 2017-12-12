import SocketServer
#import socket
import sys
import pickle
from collections import defaultdict
from player import *
import game_server
import packet

class serverUDP(SocketServer.BaseRequestHandler):

    #Adapted from source: https://docs.python.org/2/library/socketserver.html
    """
    This class works similarly to the TCP handler class, except that
    self.request consists of a pair of data and client socket, and since
    there is no connection the client address must be given explicitly
    when sending data back via sendto().
    """

    def handle_join_request(self, pack):
        if gl.players_taken == [True]*gl.num_players:
            response = packet.join_reply(False)
            pickled_response = pickle.dumps(response)
            self.request[1].sendto(pickled_response, self.client_address)
        else:
            for i in range(0,len(gl.players_taken)):
                if not gl.players_taken[i]:
                    pos = gl.player_list[i].position
                    angle = gl.player_list[i].angle
                    color = gl.player_list[i].color
                    name = pack.get_data()["name"]
                    response = packet.join_reply(True, i, pos, angle, color, gl.num_players)
                    gl.player_list[i].name = name
                    gl.players_taken[i] = True
                    print "ID "+str(i)+" was given to "+name+" on addr "+ str(self.client_address)
                    self.bind_socket_address_to_player(i, self.request[1], self.client_address)
                    self.send_packet(response, i)
                    break

        if gl.players_taken == [True]*gl.num_players:
            for i in range(0,len(address_list)):
                for j in range(0,len(gl.player_list)):
                    if i != j:
                        playr = gl.player_list[j]
                        pack = packet.initial_other_player(j, playr.name, playr.position, playr.angle, playr.color)
                        self.send_packet(pack, i)
            for i in range(0,len(address_list)):
                self.send_packet(packet.starting_game(), i)
            gl.game_started = True

    # handle(self): keeps the connection alive, adds
    def handle(self):
        data = self.request[0].strip()
        pack = pickle.loads(data)
        print pack

        packet_type = pack.get_type()
        response = None

        if packet_type == "join_request":
            self.handle_join_request(pack)
        elif packet_type == "client_update_player":
            data = pack.get_data()
            identity = data["id"]
            for p in list_of_players:
                if p.id != identity:
                    #send to pack to p
                    pack = update_other_player(data["id"], data["position"], data["angle"], data["lives"])
                    pickled_pack = pickle.dumps(pack)
                    socket.sendto()
                    pass
            pass
        elif packet_type == "leaving_game":
            identity = pack.get_data()["id"]
            gl.players_taken[identity] = False



    def bind_socket_address_to_player(self, p_id, socket, addr):
        address_list[p_id] = addr
        socket_list[p_id] = socket

    def send_packet(self, pack, player_id):
        pickle_pack = pickle.dumps(pack)
        socket_list[player_id].sendto(pickle_pack, address_list[player_id])

    def receive_packet(self):
        #return packet
        pass

    def remove_dead_player(self, player_list):
        for key in gl.player_list.copy().iterkeys():
            player = gl.player_list[key]
            if (player.lives < 1):
                del gl.player_list[key]
        return gl.player_list



    def check_collision(self, p1, p2):
        x_distance = p1.position[0] - p2.position[0]
        y_distance = p1.position[1] - p2.position[1]
        distance = math.sqrt(x_distance**2 + y_distance**2)
        if distance < p1.radius+p2.radius:
           return True
        return False


def start_server():

    global address_list
    global socket_list
    global gl
    #new= MyUDPHandler()
    gl = game_server.gamelogic()

    address_list = [None]*gl.num_players
    socket_list = [None]*gl.num_players
    print "game_server set up."
    HOST, PORT = "localhost", 8080
    server = SocketServer.UDPServer((HOST, PORT), serverUDP)
    print "Socket set up."
    print "Wating for players to Join..."
    server.serve_forever()



start_server()
#server.handle()
