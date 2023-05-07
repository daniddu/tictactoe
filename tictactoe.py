from random import *

def player_move(board, mark, position):
    # Returns the game board with the given mark in the given position.
    board = board
    position = position
    mark = mark
    
    if board[position] == "-":
        if 0 <= position <= 20:
            board = board[0:(position - 1)] + mark + board[(position + 1):20]
            return(board)
        else:
            print("no valid value")
    else:
        print("sorry occupied")
       

def pc_move(board):
    board = board
    print(board)
    position = randrange(0,19)
    print(position)
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
position = int(input("enter position for you mark: "))
mark = input("enter mark: ")

board = player_move(board, mark, position)
print(board)
board = pc_move(board)
print(board)
