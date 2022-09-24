

import numpy as np
import Board
import Winning_move
import random
import minmax
x_axis = Board.x_axis
y_axis  = Board.y_axis
 



     
board = Board.board()
Board.print_board(board)
end_of_the_game = True
turn = 0
 
while end_of_the_game:
    if turn == 0:
        move = int(input("Player 1, Make your Selection(0-6):"))

        if move < 0 or move > 6: #If we select a wrong slot
            print("Please select a proper slot!")
            continue

        if move in minmax.thisdict:  #This will check if the slot is full or not (max is 7)
            if minmax.thisdict[move] == 6:
                print("Please select another slot since this is FULL!")
                continue
        if move not in minmax.thisdict: #We will use a dict, since it is a lot easier and faster to do this way
            minmax.thisdict[move] = 1
        else:
            minmax.thisdict[move] = minmax.thisdict[move] + 1


        
        if Board.is_valid(board,move):
            row = Board.get_next_open_row(board,move)
            Board.move(board,row,move,1)
      #      Board.print_board(board)
            if Winning_move.win(board, 1): #We check if it is a winning game!
                        print("Player 1 wins!")
                        end_of_the_game = False
         

    else: #The A.I (sort of)

       minimax_max = minmax.minimax(board)

       break

        

       #predict = minmax.players_next_move(board)
       # if predict == -10:
       #     move = random.randint(0,6)
       # else:
       #     move = predict
       # if move in minmax.thisdict:  #This will check if the slot is full or not (max is 7)
       #     if minmax.thisdict[move] == 6:
       #         continue
       # if move not in minmax.thisdict: #We will use a dict, since it is a lot easier and faster to do this way
       #     minmax.thisdict[move] = 1
       # else:
       #     minmax.thisdict[move] = minmax.thisdict[move] + 1
        
        #Player 2 will drop a piece on the board
       # if Board.is_valid(board,move):
       #     row = Board.get_next_open_row(board,move)
       #     Board.move(board,row,move,2)
       #     Board.print_board(board)
       #     if Winning_move.win(board, 2):
       #                 print("Player 2 wins!")
       #                 end_of_the_game = False
 
    Board.print_board(board) # We need to print it the matrix upside down
             
    turn += 1
    turn = turn % 2