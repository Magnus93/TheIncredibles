class packet:
    def __init__(self, packet_type, data={}):
        self.packet_type = packet_type
        self.data = data    # As a dictionary

    def get_type(self):
        return self.packet_type

    def get_data(self):
        return self.data

    def __str__(self):
        return "Packet type: "+self.packet_type+"\n\t"+str(self.data)

###################################
######## Client -> Server #########
###################################

# Client -> Server
def join_request(name):
    data = {"name":name}
    return packet("join_request", data)


# Client -> packet
def accepted_other_player(identity):
    data = {"id":identity}
    return packet("accepted_other_player", data)

# Client -> Server
def client_update_player(position, angle, lives, velocity):
    data = {"position":pos, "angle":angle, "lives":lives, "velocity": velocity}
    return packet("client_update_player", data)

def leaving_game(identity):
    data = {"id":identity}
    return packet("leaving_game", data)

###################################
######## Server -> Client #########
###################################

# Server -> Client
def join_reply(bool_answer, identity=-1, pos=(0,0), angle=0, color=(0,0,0), num_players=0):
    data = {"answer":bool_answer, "id":identity, "position":pos, "angle":angle, "color":color, "num_players": num_players}
    return packet("join_reply", data)

# Server -> Client
def initial_other_player(identity, name, pos, angle, color):
    data = {"id": identity ,"name":name, "position":pos, "angle":angle, "color":color}
    return packet("initial_other_player", data)


def starting_game():
    return packet("starting_game")

# Server -> Client
def update_other_player(identity, position, angle, lives):
    data = {"id":identity, "position":pos, "angle":angle, "lives":lives}
    return packet("update_other_player", data)

# Server -> Client
def player_collision(identity_of_other_player):
    data = {"id": identity_of_other_player}
    return packet("player_collision", data)
