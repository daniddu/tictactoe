from random import *

def player_move(board):
    # Returns the game board with the given mark in the given position.
    position = int(input("enter position for you mark: "))
    mark = input("enter mark: ")
    
    if (board[position]) != "-":
        print("sorry occupied")
    else:       
        if 0 <= position <= 20:
            board = board[0:(position - 1)] + mark + board[(position):20]
        else:
            print("no valid value")
    return(board)

def pc_move(board):
    position = randrange(0,19)
    print(position)
    mark = "o"

    if (board[position]) != "-":
        print("sorry occupied")
    else:       
        if 0 <= position <= 20:
            board = board[0:(position - 1)] + mark + board[(position):20]
        else:
            print("no valid value")
    return(board)


board = "-"*20
while board.count("-") > 0:
    board = player_move(board)
    board = pc_move(board)
    print(board)
else:
    print("finish")
