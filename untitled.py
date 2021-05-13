
import numpy
board=numpy.array([['-','-','-'],['-','-','-'],['-','-','-']])
p1="X"
p2="O"
def won(symbol):
    return check_row(symbol) or check_col(symbol) or check_diagonal(symbol)

def check_row(symbol):
    for r in range(3):
        count=0
        for c in range(3):
            if board[r][c]==symbol:
                count+=1
        if(count==3):
            print(symbol,"won")
            return True
    return False

def check_col(symbol):
    for r in range(3):
        count=0
        for c in range(3):
            if board[c][r]==symbol:
                count+=1
        if(count==3):
            print(symbol,"won")
            return True
    return False
    
def check_diagonal(symbol):
    if(board[0][2]==board[1][1] and board[1][1]==board[2][0] and board[2][0]==symbol):
        print(symbol,"won")
        return True
    if(board[0][0]==board[1][1] and board[1][1]==board[2][2] and board[2][2]==symbol):
        print(symbol,"won")
        return True
    return False


def place(symbol):
    print(numpy.matrix(board))
    while(1):
        row=int(input("Enter row - 1,2 or 3 "))
        col=int(input("Enter col - 1,2 or 3 "))
        if(row>0 and row<4 and col>0 and col<4 and board[row-1][col-1]=="-"):
            break
        else:
            print("invalid input!!try again")
    board[row-1][col-1]=symbol

def play():
    for i in range(9):
        if i%2==0:
            print("X turn")
            place(p1)
            if won(p1):
                break
        else:
            print("O turn")
            place(p2)
            if won(p2):
                break
    if not(won(p1)) and not(won(p2)):
        print("Draw")    
play()