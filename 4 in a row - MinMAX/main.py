

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
        if Board.is_valid(board,move):
            row = Board.get_next_open_row(board,move)
            Board.move(board,row,move,1)
      #      Board.print_board(board)
            if Winning_move.win(board, 1):
                        print("Player 1 wins!")
                        end_of_the_game = False
         

    else:
        predict = minmax.players_next_move(board)
        if predict == -10:
            move = random.randint(0,6)
        else:
            move = predict
        
        #Player 2 will drop a piece on the board
        if Board.is_valid(board,move):
            row = Board.get_next_open_row(board,move)
            Board.move(board,row,move,2)
            Board.print_board(board)
            if Winning_move.win(board, 2):
                        print("Player 2 wins!")
                        end_of_the_game = False
 
    Board.print_board(board) # We need to print it the matrix upside down
             
    turn += 1
    turn = turn % 2