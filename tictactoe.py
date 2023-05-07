def player_move(board, mark, position):
    # Returns the game board with the given mark in the given position.
    my_board = board
    print(my_board)
    my_position = position
    print(my_position)
    my_mark = mark
    print(my_mark)

    if 0 <= my_position <= 20:
        if my_board[my_position] == "-":
            my_board = my_board[5].replace("-", my_mark)
            print(my_board)
        else:
            print("sorry occupied")

    else:
        print("no valid value")

    
board = "-"*20
position = int(input("enter position for you mark: "))
mark = input("enter mark: ")
player_move(board, mark, position)