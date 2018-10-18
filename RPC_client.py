#Tony Tran qmtran

import sys
import socket

def prompt():
    isValid = False
    options = ('R', 'P', 'S')
    
    while (isValid is False):
        rps = raw_input("\nEnter R, P, or S: ").upper()
        
        if rps in options:
            isValid = True
    return rps
  
def Main(): 
    # get game host IP from command argument
    host = sys.argv[1]
  
    # get port to connect from command argument
    port = int(sys.argv[2])
  
    # create socket
    s = socket.socket(socket.AF_INET,socket.SOCK_STREAM) 
  
    # connect to game server
    s.connect((host,port)) 
  
    # get connection verifying message from the server
    message = s.recv(1024)
    print (message)
    
    # get player number from the server
    player = int(s.recv(1024))
    print "You are Player", player
    
    # if first player, wait for second player
    if player == 1:
        print "Waiting for a second player to join."
    # if second player, ready to play 
    elif player == 2:
        print "Let's play!"
    # if neither first or second, can't join the game and disconnects
    elif player > 2:
        print "Server is busy with game. Please connect later."
        exit(0)
    
    #get client input for game R,P, or S
    clientInput = prompt()
    choice = clientInput
    choice += str(player)
    
    #if input received, send it to server
    if clientInput:
        s.send(choice)
    
    # gets the game result from the server
    result = s.recv(1024)
    
    # if 0, game is a tie
    # if it matches client's player number, won
    # if not, lost
    if result == '0':
        print "Tie"
    elif int(result) == player:
        print "You won!"
    else:
        print "You lost!"
    
    # gets farewell message from the server
    print(s.recv(1024))
    
    # close the connection 
    s.close() 
  
if __name__ == '__main__': 
    Main() 