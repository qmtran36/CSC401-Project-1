import csv
import sys

port = sys.argv[1]

print(port)
def main():
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	#Starting game server
	print ("Server is ready to serve!\n")

#Client A connected as player 1
print ("A new player is trying to connect to the game server on ")
print ("Current number of available players is 1")
print ("One player waiting for another player to join\n")

#Client B connected as player 2
print ("A new player is trying to connect to the game server on ")
print ("Current number of available players is 2")

#Game begin Client A and B begins
print ("New Game Thread spawned")

#Client A chose R, P or S
print ("Player 1 played: \n")

#Client C is trying to connect while server is busy.
print ("A new player is trying to connect to the game server on ")
print ("Two players are already. Can't start a new game.\n")

#Client B chose R, P or S
print ("Player 2 played: \n")

#Game begin Client A and B continues and finishes.
print ("Player # won!")
print ("Game over.")