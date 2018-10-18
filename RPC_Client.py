import sys
import socket

#Obtain valid RPS move from user
def getInput():  
  while 1:
    response = raw_input("Enter R, P, or S: ")
    if response == 'R' or response == 'P' or response == 'S':
      return response

#Obtain IP and port from command line
ipAddress = sys.argv[1]
tcpPort = int(sys.argv[2])

#Create socket and connect to remote
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((ipAddress, tcpPort))

try:
  #Print the connection verification message
  verify = client.recv(1024)
  print verify

  #Store player count from server
  count = int(client.recv(1024))
  
  #Stay and play or exit depending on count
  if count <= 2:
    print "You are Player",count,"."
    if count == 1:
      print "Waiting for a second player to join.\n"
    elif count == 2:
      print ("Let's play!\n")

    #Send choice to server
    move = getInput()
    client.send(move)

    #Get Win, Loss, Tie
    result = client.recv(1024)
    print result

    print "Disconnecting from the game server. Thank you for playing!"
  else: #Count more than 2
    msg = client.recv(1024)
    print msg
finally:
  client.close()