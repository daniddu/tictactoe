from random import *

def player_move(board):
    # Returns the game board with the given mark in the given position.
    position = int(input("enter position for you mark: "))
    mark = input("enter mark: ")
    board = board
    
    while board[position] == "-":
        if 0 <= position <= 20:
            board = board[0:(position - 1)] + mark + board[(position + 1):20]
        else:
            position = 0
            print("no valid value")
    else:        
        print("sorry occupied")
    return(board)
 

def pc_move(board):
    board = board
    position = randrange(0,19)
    mark = "o"
    if board[position] == "-":
        if 0 <= position <= 20:
            board = board[0:(position - 1)] + mark + board[(position + 1):20]
            return(board)
        else:
            print("no valid value")
    else:
        print("sorry occupied")



board = "-"*20

board = player_move(board)
print(board)
board = pc_move(board)
print(board)
