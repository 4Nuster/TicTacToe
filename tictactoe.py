import numpy as np

board = np.array([[0, 0, 0], [0, 0, 0], [0, 0, 0]])
playX = 3
playY = 3
player = 0

def fill(i, j):
    if(board[i][j] == 1): return "X"
    elif(board[i][j] == 2): return "O"
    else: return " "

def printer():
    global playX
    playX = 3
    print("\n\n\n")
    for i in range(0, 3):
        print(fill(i, 0)+" | "+fill(i, 1)+" | "+fill(i, 2))
        if(i != 2): print("----------")

def inputer():
    global playX, playY, player, board
    #printer()
    while(playX == 3):
        print("\n")
        tempX = input("Your turn Player "+str((player % 2)+1)+", X axis: ")
        tempY = input("Y axis: ")
        if((tempX!="0" and tempX!="1" and tempX!="2") or (tempY!="0" and tempY!="1" and tempY!="2")):
            print("Please enter a valid position: ")
        elif(board[int(tempX)][int(tempY)] != 0):
            print("Position occupied!!!!!")
            playX = 3
        else:
            playX = tempX
            playY = tempY
    
    board[int(playX)][int(playY)] = int((player % 2)+1)
    player+=1

def winning():
    if(board[0][0] == board[0][1] and board[0][1] == board[0][2] and board[0][0] != 0): tempWinner = board[0][0]
    elif(board[1][0] == board[1][1] and board[1][1] == board[1][2] and board[1][0] != 0): tempWinner = board[1][0]
    elif(board[2][0] == board[2][1] and board[2][1] == board[2][2] and board[2][0] != 0): tempWinner = board[2][0]
    elif(board[0][0] == board[1][0] and board[1][0] == board[2][0] and board[0][0] != 0): tempWinner = board[0][0]
    elif(board[0][1] == board[1][1] and board[1][1] == board[2][1] and board[0][1] != 0): tempWinner = board[0][1]
    elif(board[0][2] == board[1][2] and board[1][2] == board[2][2] and board[0][2] != 0): tempWinner = board[0][2]
    elif(board[0][0] == board[1][1] and board[1][1] == board[2][2] and board[0][0] != 0): tempWinner = board[0][0]
    elif(board[0][2] == board[1][1] and board[1][1] == board[2][0] and board[0][2] != 0): tempWinner = board[0][2]
    else: tempWinner = 0
    return tempWinner

def full():
    if(board[0][0]!=0 and board[0][1]!=0 and board[0][2]!=0 and board[1][0]!=0 and board[1][1]!=0 and board[1][2]!=0 and board[2][0]!=0 and board[2][1]!=0 and board[2][2]!=0):
        return True
    else: return False


#printer()
while(not full() and winning() == 0):
    printer()
    inputer()

print("\n\n\n")
if(winning() != 0): 
    printer()
    print("\nTHE WINNER IS PLAYER "+str(winning()))
else: print("DRAW")

