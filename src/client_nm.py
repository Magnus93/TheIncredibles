import socket
import sys
import pickle
from collections import defaultdict
from player import *

#source: https://pymotw.com/2/socket/udp.html
# Create a UDP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

server_address = ('localhost', 10000)
message = 'This is the message.  It will be repeated.'

try:

    # Send data
    print >>sys.stderr, 'sending "%s"' % message
    #sent = sock.sendto(message, server_address)

    #p = player(player_id=1, position=(300,300), color=(255,0,255), name='Nea')
    p = player(1, (300,300), (255,0,255), "Nea")
    pl=pickle.dumps(p)
    sock.sendto(pl,server_address)

    # Receive response
    print >>sys.stderr, 'waiting to receive'
    data, server = sock.recvfrom(4096)
    unpickled_playr=pickle.loads(data)
    print >>sys.stderr, 'received "%s"' % unpickled_playr.name

finally:
    print >>sys.stderr, 'closing socket'
    sock.close()
