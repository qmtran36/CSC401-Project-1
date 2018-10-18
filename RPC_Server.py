import sys
import socket
import thread

#Welcomes client depending on number of players
def welcome(ip, port, count, client):
  #Message goes to all clients
  print "A new player is trying to connect to the game server on ",ip,":",port
  client.send("Connected to the Rock, Paper, Scissors Game Server.\n")
  client.send( str(count) )
  
  if count == 1 or client == 0: #Room available
    print "Current number of available players is ",count
    print "One player waiting for another player to join.\n"
  elif count == 2: #Room available
    print "Current number of available players is ",count
    print "Two players available, let's play!\n"
  else: #No room for more players
    client.send("Server is busy with a game. Try to connect again later.\n")
    client.close()
    print "Two players already playing. Can't start a new game."

#Thread to run the game
def game_thread(playerA, playerB):
  #Obtain player's moves
  print ">>New Game Thread spawned"
  data1 = playerA.recv(1024)
  print ">>Player 1 played: ", data1
  data2 = playerB.recv(1024)
  print ">>Player 2 played: ", data2

  #Determine winner by checking tie, first player win, or second player win
  if (data1 == data2):
    print ">>Players tied!"
    playerA.send("You tied!")
    playerB.send("You tied!")
  elif (data1 == "R" and data2 == "S") or (data1 == "P" and data2 == "R") or (data1 == "S" and data2 == "P"):
    print ">>Player 1 won!"
    playerA.send("You won!")
    playerB.send("You lost!")
  else:
    print ">>Player 2 won!"
    playerA.send("You lost!")
    playerB.send("You won!")
  
  #Close client sockets and update client count
  global clientCount
  playerA.close
  playerB.close
  clientCount = 0
  print ">>Game Over.\n"

#Get the server's IP
IPAddr = socket.gethostbyname(socket.gethostname())

#Obtain port from command line
port = int(sys.argv[1])

#Create a socket, then bind it to previous port
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('',port))

#Keep 5 clients in the backlog
s.listen(5)

# No clients initially
clientCount = 0

print ("Server is ready to serve!\n")

try:
  while 1:
    #Accept first player and update count
    aSocket, aAddr = s.accept()
    clientCount += 1
    welcome(IPAddr, port, clientCount, aSocket)

    #Accept second player and update count
    bSocket, bAddr = s.accept()
    clientCount += 1
    welcome(IPAddr, port, clientCount, bSocket)

    #Run game
    thread.start_new_thread(game_thread, (aSocket,bSocket)) 

finally:
#Close server socket
s.close()