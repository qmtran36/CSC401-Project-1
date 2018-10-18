import sys
import socket
import thread

def welcome(ip, port, count, client):
  print "A new player is trying to connect to the game server on ",ip,":",port
  print "Current number of available players is ",count
  client.send("Connected to the Rock, Paper, Scissors Game Server.\n")
  client.send( str(count) )
  
  if count == 1:
    print "One player waiting for another player to join.\n"
    client.send("Waiting for a second player to join.\n")
  else:
    print ("Two players available, let's play!\n")
    client.send("Let's play!\n")
   
def game_thread(playerA, playerB):
  print ">>New Game Thread spawned"
  data1 = playerA.recv(1024)
  print ">>Player 1 played: ", data1
  data2 = playerB.recv(1024)
  print ">>Player 2 played: ", data2

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
  
  playerA.send("Disconnecting from the game server. Thank you for playing!")
  playerB.send("Disconnecting from the game server. Thank you for playing!")
  print ">>Game Over.\n"

IPAddr = socket.gethostbyname(socket.gethostname())       
print "Your Computer IP Address is:" + IPAddr

port = int(sys.argv[1])
response=[]

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('',port))
s.listen(5)
clientCount = 0

print ("Server is ready to serve!\n")
while 1:
  aSocket, aAddr = s.accept()
  clientCount += 1
  welcome(IPAddr, port, clientCount, aSocket)

  bSocket, bAddr = s.accept()
  clientCount += 1
  welcome(IPAddr, port, clientCount, bSocket)

  thread.start_new_thread(game_thread, (aSocket,bSocket))

  aSocket.close
  bSocket.close  
  clientCount = 0

s.close()