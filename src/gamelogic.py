import math
import sys
import player
import serverUDP

ID_REQUEST_JOIN = -1

p1 = player(1,(20,20),(255,0,0) ,"player1")
p2 = player(2,(40,20),(0,255,0) ,"player2")
p3 = player(3,(20,40),(0,0,255) ,"player3")
p4 = player(4,(40,40),(255,0,255),"player4")

players = [p1,p2,p3,p4]
players_taken = [False,False,False,False]

def initiate_player_and_send(receiver_client):
    for i in range(0:len(players_taken)):
        if not players_taken[i]:
            break

    if i > 3:
        print("Game is full")
        pass
    else:
        players_taken[i] = True
        # send player[i] to receiver_client
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
