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


def on_new_client(clientsocket, addr):
	count = 1
	while 1:
		msg = clientsocket.recv(1024)
        print addr, ' >> ', msg
        #Maybe some code to compute the last digit of PI, play game or anything else can go here and when you are done.
        clientsocket.send(msg)
        clientsocket.close()
	count += 1
	print("current amount of players", count)



    #clientsocket.close()

hostname = socket.gethostname()    
IPAddr = socket.gethostbyname(hostname)    
print("Your Computer Name is:" + hostname)    
print("Your Computer IP Address is:" + IPAddr) 

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

	cSocket.send( "Connected to the Rock, Paper, Scissors Game Server." ) #S1. --Connection--
	print(count)
	print(str(count))
	cSocket.send( str(count) ) #S2. --Player number
	start(IPaddress, count)
	thread.start_new_thread(on_new_client, (cSocket,address))

	data = cSocket.recv(1024) #R1. Rock, Paper, Scissor
	response.append( data )
	if count == 2:
		print ("New Game Thread spawned")
		print ("Player 1 played: ", response[0])
		print ("Player 1 played: ", response[1])
		print ("Player ", count, " won!")
		print ("Game Over.")

 	print( response )
 	print( data )
	cSocket.send(data)  # S3. 

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