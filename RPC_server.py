import sys
import socket
import thread
import array



def start(ip, player):
	print "A new player is trying to connect to the game server on ", ip
	print "Current number of available players is ", player
	if player == 1:
		print ("One player waiting for another player to join\n")
	else:
		print ("Two players available, let's play!\n")
	#return ip.recv(1024)
def on_new_client(clientsocket, player):
	player = player
	#if ( player == 1 or player == 2 ):
    	# while True:
    	# 	msg = clientsocket.recv(1024) 
    	#    	clientsocket.send(msg)

    #clientsocket.close()


port = int(sys.argv[1])
response=[]
IPaddress = socket.gethostbyname(socket.gethostname())
#create a socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# hostname = socket.gethostname() 
# IPAddr = socket.gethostbyname(hostname) 
#Starting game server
s.bind((IPaddress,port))
s.listen(1)
count = 0

print ("Server is ready to serve!\n")
while 1:
	#s.listen(1)
	cSocket, address = s.accept()

	count += 1

	cSocket.send( "Connected to the Rock, Paper, Scissors Game Server." )
	cSocket.send( str(count) )
	start(IPaddress, count)
	thread.start_new_thread(on_new_client, (cSocket,count))

	data = cSocket.recv(1024)
	response.append( data )
 	#if not data: break
 	print( response )
	cSocket.send(data)  # echo

cSocket.close()


# #Client A connected as player 1
# def calls():

# 	#Client B connected as player 2
# 	print ("A new player is trying to connect to the game server on ")
# 	print ("Current number of available players is 2")

# 	#Game begin Client A and B begins
# 	print ("New Game Thread spawned")

# 	#Client A chose R, P or S
# 	print ("Player 1 played: \n")

# 	#Client C is trying to connect while server is busy.
# 	print ("A new player is trying to connect to the game server on ")
# 	print ("Two players are already. Can't start a new game.\n")

# 	#Client B chose R, P or S
# 	print ("Player 2 played: \n")

# 	#Game begin Client A and B continues and finishes.
# 	print ("Player # won!")
# 	print ("Game over.")


# if __name__ == "__main__":
#     main()