import sys
import socket

def getInput():
	#print ("Enter R, P, or S: #")
	response = raw_input("Enter R, P, or S: ")
	if response == 'S' or response == 'P' or response == 'R':
		return response
	else:
		return "error"

ipAddress = sys.argv[1]
tcpPort = int(sys.argv[2])

cSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
cSocket.connect((ipAddress, tcpPort))

verify = cSocket.recv(1024)
print ( verify ) #Connected to server

while 1:
	player = int(cSocket.recv(1024)) 
	#player = cSocket.recv(1024)
	print "You are Player", player, "\b."

	if player == 1:
		print ("Waiting for a second player to join.\n")
		responseOne = getInput()
		#print(responseOne)
		cSocket.send( responseOne )

	if player == 2:
		print ("Lets play!\n")
		responseTwo = getInput()
		#print(responseTwo)
		cSocket.send( responseTwo )

#while 1:

#cSocket.send("Hi how are you?")
result = cSocket.recv(1024)
#print( result )
cSocket.close()



#Post Game message
print ("Disconnecting from the game server. Thank you for playing!")

# def ClientA():#Client A or Player 1
# 	print ("Connected to the Rock, Paper, Scissors Game Server.")
# 	print ("You are player #.")
# 	print ("Waiting for a second player to join.\n")

# def ClientB():#Client B or Player 2
# 	print ("Connected to the Rock, Paper, Scissors Game Server.")
# 	print ("You are player #.")
# 	print ("Lets play!\n")

def ClientC():#Client C or Player 3
	print ("Enter R, P, or S: #")
	print ("Result of the game is 2")
	print ("You Won!\n")#"You Lost!"


