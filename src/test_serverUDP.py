import socket
import sys
import pickle
from collections import defaultdict 
from player import * 
from serverUDP import *
#from server import *

p1 = player(1, (300,300), (255,0,255), "A") 
p2 = player(2, (300,300), (255,0,255), "B") 
p3 = player(3, (300,300), (255,0,255), "C") 
p4 = player(4, (300,300), (255,0,255), "D") 
p5 = player(5, (300,300), (255,0,255), "E") 
dict = {}

dict[p1.player_id]=p1
dict[p2.player_id]=p2
dict[p3.player_id]=p3
dict[p4.player_id]=p4
dict[p5.player_id]=p5

for k in dict:
	print dict[k].player_id

address={}
a1= '12'
a2= '56'
a3= '78'
a4= '91'
address[a1]=a1
address[a2]=a2
address[a3]=a3
address[a4]=a4

for k in address:
	print address[k]
player_list = {}
address_list = {}
start_server()