import math
import sys
import player


ID_REQUEST_JOIN = -1

class gamelogic:


    def __init__(self):

        self.num_player = 2
        p1 = player.player(0,(20,20),(255,0,0) ,"player0")
        p2 = player.player(1,(780,780),(0,255,0) ,"player1")
        p3 = player.player(2,(20,780),(0,0,255) ,"player2")
        p4 = player.player(3,(780,20),(255,0,255),"player3")
        
        self.player_list = [p1,p2,p3,p4]
        self.player_list = self.player_list[:self.num_player]
        self.players_taken = [False]*self.num_player


def initiate_player_and_send():
    for i in range(0,len(players_taken)):
        if not players_taken[i]:
            break

    if i > self.num_player-1:
        print("Game is full")
        pass
    else:
        players_taken[i] = True
        # send player[i] to receiver_client
        pass


def wait_for_start(self):
    pass



def main():
    serv = serverUDP.serverUDP()
    # Wait for players to join


    #Run game

    for p in players:
        for a in players:
            if p.id == a.id:
                pass
            else:
                p.check_hit_from_other(a)
        pass

    pass




if __name__ == '__main__':
    main()
