import SocketServer
#import socket
import sys
import pickle
from collections import defaultdict
from player import *
import gamelogic

class serverUDP(SocketServer.BaseRequestHandler):

    #Adapted from source: https://docs.python.org/2/library/socketserver.html
    """
    This class works similarly to the TCP handler class, except that
    self.request consists of a pair of data and client socket, and since
    there is no connection the client address must be given explicitly
    when sending data back via sendto().
    """

    def handle_join(self, unpickled_data):
        for i in range(0,len(gl.players_taken)):
            if not gl.players_taken[i]:
                break
        if gl.players_taken == [True]*gl.num_player:
            print "Game is full"
        else:
            print "player request granted for id " + str(i)
            gl.players_taken[i] = True
            for p in gl.player_list:
                print "id "+str(p.id)
            gl.player_list[i].name = unpickled_data.name
            print "i is "+str(i)
            gl.player_list[i].id = i
            print ""
            print str(i)
            address_list[i] = self.client_address


    # handle(self): keeps the connection alive, adds
    def handle(self):
        data = self.request[0].strip()

        unpickled_data= pickle.loads(data)


        if unpickled_data.id == -1:
            for i in range(0,len(gl.players_taken)):
                if not gl.players_taken[i]:
                    break

            if gl.players_taken == [True]*gl.num_player:
                print("Game is full")
                pass
            else:
                print "player request granted for id " + str(i)
                gl.players_taken[i] = True
                for p in gl.player_list:
                    print "id "+str(p.id)

              #  gl.player_list[i] = gl.players[i]
                gl.player_list[i].name = unpickled_data.name
                #print "i is "+str(i)
                gl.player_list[i].id = i
                #print ""
                #print str(i)
                address_list[i] = self.client_address
        #print "in my player list now: "
        #for p in gl.player_list:
         #   print p
        #gl.player_list[unpickled_data.id] = unpickled_data

        socket = self.request[1]

        if gl.players_taken == [True]*gl.num_player:
            pass
            #print("game started")
            #gl.player_list[unpickled_data.id] = unpickled_data
            # Check collisions for gl.player_list
            #gl.player_list

        #update list of addresses (client addresses) from any incoming connection
        #address_list[self.client_address[0]]= self.client_address
        #print address_list

        #self.remove_dead_player(player_list)


        for p in gl.player_list:
            if unpickled_data.id == p.id:
                p.position = unpickled_data.position
                p.angle = unpickled_data.angle
                p.bullets = unpickled_data.bullets


        if self.check_collision(gl.player_list[0], gl.player_list[1]):
            if not gl.player_list[0].immortal:
                print ("krokc")
                gl.player_list[0].lives -=1
                if not gl.player_list[1].immortal:
                    gl.player_list[1].lives -=1
            ####Set immortal och immortal_timer#############
            ############################################


        players_pickled = pickle.dumps(gl.player_list)

        for addr in address_list:
            #print address_list[k]
            #send all players not just data.upper
            if addr:

                socket.sendto(players_pickled, addr)  #data.upper()

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
            #tmp_speed = p1.speed
            #p1.speed = p2.speed
            #p2.speed = tmp_speed
            #p1.take_damage()
            #p2.take_damage()


def start_server():

    global address_list
    global gl
    #new= MyUDPHandler()
    gl = gamelogic.gamelogic()
    address_list=[None]*gl.num_player
    HOST, PORT = "localhost", 8080
    server = SocketServer.UDPServer((HOST, PORT), serverUDP)
    server.serve_forever()



start_server()
#server.handle()
