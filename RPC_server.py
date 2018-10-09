import sys
#from socket import *
import socket

port = int(sys.argv[1])
#create a socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print(port)
# hostname = socket.gethostname() 
# IPAddr = socket.gethostbyname(hostname) 
#Starting game server
s.bind((socket.gethostname(),port))
s.listen(1)

print ("Server is ready to serve!\n")
while 1:
	cSocket, address = s.accept()
	char = connectionSocket.recv(1024)
	cSocket.send(char)
	cSocket.close()
#addr_size = sizeof their_addr;
#new_fd = accept(sockfd, (struct sockaddr *)&their_addr, &addr_size);

#calls()

#def main():
	# #create a socket
	# serverSocket = socket(AF_INET, SOCK_STREAM)
	# #hostname = socket.gethostname() 
	# #IPAddr = socket.gethostbyname(hostname) 
	# #print(hostname)
	# #print(IPAddr)
	# #Starting game server
	# serverSocket.bind(port)
	# serverSocket.listen(1)

	# #addr_size = sizeof their_addr;
	# #new_fd = accept(sockfd, (struct sockaddr *)&their_addr, &addr_size);
	# print ("Server is ready to serve!\n")
	# #calls()

# #Client A connected as player 1
# def calls():
# 	print ("A new player is trying to connect to the game server on ")
# 	print ("Current number of available players is 1")
# 	print ("One player waiting for another player to join\n")

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