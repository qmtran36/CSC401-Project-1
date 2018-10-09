import sys
import socket

ipAddress = sys.argv[1]
tcpPort = int(sys.argv[2])

cSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
cSocket.connect((ipAddress, tcpPort))

print(ipAddress)
print(tcpPort)

#Post Game message
print ("Disconnecting from the game server. Thank you for playing!\n")

def ClientA():#Client A or Player 1
	print ("Connected to the Rock, Paper, Scissors Game Server.")
	print ("You are player #.")
	print ("Waiting for a second player to join.\n")

def ClientB():#Client B or Player 2
	print ("Connected to the Rock, Paper, Scissors Game Server.")
	print ("You are player #.")
	print ("Lets play!\n")

def ClientC():#Client C or Player 3
	print ("Enter R, P, or S: #")
	print ("Result of the game is 2")
	print ("You Won!\n")#"You Lost!"


