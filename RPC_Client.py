import sys
import socket

def getInput():  
  while 1:
    response = raw_input("Enter R, P, or S: ")
    if response == 'R' or response == 'P' or response == 'S':
      return response

ipAddress = sys.argv[1]
tcpPort = int(sys.argv[2])

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((ipAddress, tcpPort))

verify = client.recv(1024)
print verify

while 1:

  count = int(client.recv(1024))
  print "You are Player",count, "."

  ready = client.recv(1024)
  print ready

  move = getInput()
  client.send(move)

  result = client.recv(1024)
  print result

  end = client.recv(1024)
  print end

  client.close()