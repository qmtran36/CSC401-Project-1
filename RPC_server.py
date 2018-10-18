#Tony Tran qmtran

import sys
import socket
import thread
import array



lock = thread.allocate_lock() 
# players input
p1 = ''
p2 = ''
# store number of clients
clientCount = 0

# thread fuction 
def threaded(c, player):
    global p2
    global p1
    global clientCount
    
    #data is player's game input from client
    data = c.recv(1024) 
    
    # game input string contains client's number
    # prints clients game input
    if '1'in data:
        p1 = data[:1]
        print ">>Player 1 played: ", p1
    else:
        p2 = data[:1]
        print ">>Player 2 played: ", p2

    # locks the thread until other client plays
    # if already locked, that means one player already made a choice, so release the lock
    if(lock.locked() == False):
        lock.acquire()
    elif(lock.locked() == True):
        lock.release()
    
    # calculate the result of the game
    with lock:
        result = -1        
        
        #same choice, game ties
        if p1 == p2:
            result = 0
        #if not the same choice, results indicates the winner
        else:
            if p1 == 'R' and p2 == 'P':
                result = 2
            elif p1 == 'R' and p2 == 'S':
                result = 1
            elif p1 == 'P' and p2 == 'S':
                result = 2
            elif p1 == 'P' and p2 == 'R':
                result = 1
            elif p1 == 'S' and p2 == 'R':
                result = 2
            elif p1 == 'S' and p2 == 'P':
                result = 1
        
        if player == 1:
            if (result == 0):
                print ">>Tie!"
            else:
                print ">>Player ", result, "won!"
        else:
            print ">>Game Over!\n"
        
        # let the client know the winner of the game
        c.send(str(result))
        # sends the farewell message to client
        c.send("Disconnecting from the game server. Thank you for playing!")
        #close the connection
        c.close()
        #decrement the client count, so the server can take other clients to join!
        clientCount -= 1
    return
  
def Main():
    # get ip address of host
    host = socket.gethostbyname(socket.gethostname())
    print ("Game server address: ",host)
    
    # get port number from command line argument
    port = int(sys.argv[1])
    
    # create welcome socket, and bine
    # Ready to Serve!
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
    s.bind((host, port)) 
    print("Server is ready to serve!\n") 
  
    #waiting for client to join!
    s.listen(5) 
  
    global clientCount

    while True:
        #take a client!
        c, addr = s.accept()
        # prints client's adress and port number
        print "A new player is trying to connect to the game server on ", addr[0], ":", addr[1] 
        
        # increment client count, so we can play when 2 joins
        clientCount += 1
        
        # send welcome message to client, and player number
        c.send( "Connected to the Rock, Paper, Scissors Game Server." )
        c.send(str(clientCount))
        
        # print status, and start game thread if player is #1 or 2
        print "Current number of available player is ", clientCount
        if clientCount == 1:
            print "One player is waiting for another player to join\n"
            thread.start_new_thread(threaded, (c, clientCount))
        elif clientCount == 2:
            print "Two players available. Let's play!\n"
            print ">>New Game Thread spawned"
            thread.start_new_thread(threaded, (c, clientCount))
        # if third client joins, let client know that server is busy, and disconnect
        elif clientCount > 2:
            print "Two players already playing. Can't start a new game"
            #decrement count 
            clientCount -= 1
            c.close()
            
    s.close()
    exit(0)

  
if __name__ == '__main__': 
    Main() 