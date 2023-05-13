from random import *


def evaluate(board):
    if "xxx" in board:
        return("x")
    elif "ooo" in board:
        return("o")
    elif not "-" in board:
        return("!")
    else:
        return("-")

def move(board, mark, position):
    board = board[0:(position)] + mark + board[(position + 1):20]  
    return(board)

def player_move(board):
    while True:
        try:
            mark = input("enter mark: ")
            position = int(input("enter position: ")) - 1
            if position >= 20:
                print("too large")
            elif position < 0:
                print("too small")    
            elif board[position] == "-":
                board = move(board, mark, position) 
                return(board)
            elif board[position] != "-":
                print("occupied")
        except ValueError:
            print("no valid value")

def pc_move(board):
    while True:
        mark = "o"
        position = randrange(0,19)
        if board[position] == "-":
            board = move(board, mark, position)
            return(board)

def oneD_tictactoe(board):
    while True:
        board = player_move(board)
        board = pc_move(board)
        print(board)
        result = evaluate(board)

        if result == "-":
            continue
        elif result == "x":
            print("you winner")
            break
        elif result == "o":
            print("pc winner")
            break
        elif result == "!":
            print("full")
        
        
board = "-"*20
oneD_tictactoe(board)   

