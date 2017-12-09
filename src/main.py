import pygame
import sys
import player
#import client

ID_REQUEST_JOIN = -1

def request_new_player(player_name):
	# Returns new player from server
	# player.name = player_name
	pass

def wait_for_start():
	print("Waiting for other players...")
	# return otherplayers
	pass

def main():

	# Ask name
	player_name = raw_input("What is your name?: ")
	my_client = client()
	my_client.player = player(ID_REQUEST_JOIN, (0,0), (1,1,1), player_name)
	my_client.send_player()
	# Get player ID from server
	# Get color from server
	# Get position from server
	my_client.receive_players()


	# Create player
	me = request_new_player(player_name)

	# Wait for game to begin
	other_players = wait_for_start()


	while True:
		me.run()
		for p in other_players:
			p.draw()




if __name__ == '__main__':
	main()
