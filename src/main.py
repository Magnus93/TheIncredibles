import pygame
import sys
import player
#import client



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

	# Get player ID from server
	# Get Color from server
	# Get position from server

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
