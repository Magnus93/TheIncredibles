import socket
import sys
import pickle
from collections import defaultdict
from player import *
'''
# Create a UDP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Bind the socket to the port
server_address = ('130.238.243.151', 10000)
print >>sys.stderr, 'starting up on %s port %s' % server_address
sock.bind(server_address)

while True:
    print >>sys.stderr, '\nwaiting to receive message'
    data, address = sock.recvfrom(4096)

    print >>sys.stderr, 'received %s bytes from %s' % (len(data), address)
    # address (130. ... .25, port av client)
    print >>sys.stderr, data
    print(type(data))

    if data:
    #    playr=clientsock.recv(4096)
        print "Welcome!!"
        unpickled_playr=pickle.loads(data)
        #print unpickled_playr.position
        sent = sock.sendto(data, address)
        print >>sys.stderr, 'sent %s bytes back to %s' % (sent, address)
'''

def init_connection_recive(host_ip, port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    server_address = (host_ip, port)
    print >>sys.stderr, 'starting up on %s port %s' % server_address
    sock.bind(server_address)

    return sock

def init_connection_send(host_ip, port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    server_address = (host_ip, port)
    return sock

def listen_for_player(socket):
    data, address = socket.recvfrom(4096)

    unpickled_playr=pickle.loads(data)
    return unpickled_playr

def send_player(socket, playr, server_address):
    pickle_player = pickle.dumps(playr)
    socket.sendto(pickle_player, server_address)

def main():
    sock_r = init_connection_recive('130.238.243.151', 10000)
    send_address = ('130.238.250.25', 8080)
    sock_s = init_connection_send(send_address[0], send_address[1])
    p2 = player(2, (100,400), (255,0,0), "Arne")

    received = False
    while not received:
        p1 = listen_for_player(sock_r)
        print p1
        print p1.name
        if p1:
            received = True

    while True:
        send_player(sock_s, p2, send_address)


if __name__ == '__main__':
    main()
