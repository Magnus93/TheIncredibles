
import socket
from player import *


class mysocket:
	def __init__(self, max_players, serverport, my_id = None, serverhost = None):
		self.debug = 0
		self.max_players = int(max_players)
		self.serverport = int(serverport)
		if serverhost: 
			self.serverhost = serverhost
		else: 
			self.serverhost = socket.gethostname()
		if my_id: 
			self.my_id = my_id
		else:
			self.my_id = '%s:%d' % (self.serverhost, self.serverport)
		self.players = {}
		self.shutdown = False

		self.handlers = {}
		self.router = None
	def add_player(self, player):
		a = player.player_id
		self.players.update({'player'+str(a):a})
		print (self.players)

	def handle_player(self, clientsock):
		print('Connected' + str(clientsock.getpeername()))
		host, port = clientsock.getpeername()
		peerconn = BTPeerConnection(None, host, port, clientsock, debug=False)

		try:
			msgtype, magdata = peerconn.recvdata()
			if msgtype: 
				msgtype = msgtype.upper()
			if msgtype not in self.handlers:
				self.__debug('Not handled:%s: %s' % (msgtype, msgdata))
			else:
				self.__debug('Handling peer msg: %s' % (msgtype, msgdata))
				self.handlers[msgtype](peerconn, msgdata)
		except KeyboardInterrupt:
			raise
		except:
			if self.debug:
				traceback.print_exc()
		self.__debug('Disconnecting ' + str(clientsock.getpeername()))
		peerconn.close()

	def connectandsend(self, host, port, msgtype, msgdata, pid=None, waitreply=True):
		msgreply = []
		try:
			peerconn = BTPeerConnection(pid, host, port,debug = self.debug)
			peerconn.senddata(msgtype, msgdata)
			print('Sent %s: %s' % (pid, msgtype))

			if waitreply:
				onereply - peerconn.recvdata()
				while(onereply != (None, None)):
					msgreply.append(onereply)
					self.debug('Got reply %s: %s' % (pid, str(msgreply)))
					onereply = peerconn.recvdata()
			peerconn.close()
		except KeyboardInterrupt:
			raise
		except:
			if self.debug:
				traceback.print_exc()
		return msgreply


	def sendtopeer(self, peerid, msgtype, msgdata, waitreply=True):
		if self.router:
			nextpid, host, port = self.router(peerid)
		if not self.router or not nextpid:
			self.__debug('Unable to route %s to %s' % (msgtype, peerid))
			return None
		return self.connectandsend(host, port, msgtype, msgdata, pid =nextpid, waitreply=waitreply)

	def makeserversocket(self, port, backlog = 5):
		s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
		s.bind(('', port))
		s.listen(backlog)
		return s
	def makeclientsocket(self, port):
		s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		clientsocket.connect(('localhost', 8080))
		msg = raw_input('type anything and click enter... ')
		clientsocket.send(msg)


	def mainloop(self):
		s = self.makeserversocket(self.serverport)
		s.settimeout(2)
		print(str(self.my_id))
		print(str(self.serverhost))
		print(str(self.serverport))

		x = self.serverport
		print('Server started: %s (%s:%d)' % (self.my_id, self.serverhost, x))

		while not self.shutdown:
			try:
				print('Listening for connections....')
				
				clientsock, clientaddr = s.accept()
				print('accept')
				clientsock.settimeout(None)
				player_id = clientsocket.recvdata(64)
				print(player_id)
			

				#pos, pos1 = clientsocket.recv(p.position)
				#col,col1 = clientsocket.recv(p.color)
				#name = clientsocket.recv(p.name)
				#player_to_add = player(player_id, (pos,pos1), (col, col1), name)	
				#s.add_player(p)
				#print(s.players)
				#buf = clientsock.recv(64)
				#if buf>0:
					#print buf
				
				t = thereading.Thread(target = self.handle_player, args = [clientsock])
				t.start()
				print("running")
			except KeyboardInterrupt:
				self.shutdown = True
				continue
			except:
				if self.debug:
					traceback.print_exc()
					continue

		print('Main loop exiting')
		s.close()

s = mysocket(3, 8080, None, None)
p = player(1, (300,300), (255,0,255), "Nea") 
s.add_player(p)

s.mainloop()
s.handle_player(s)
	