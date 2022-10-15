



import numpy as np
import Board
import Winning_move
import random
import minmax
import sys
import math
import time
x_axis = Board.x_axis # determine the length of the rows
y_axis  = Board.y_axis # determine the length of the columns
 





def main(board):     
    how_many_turns = 0
    Board.print_board(board)
    end_of_the_game = True
    turn = 0
    Time_list = []
    while end_of_the_game: #If we reach to either a winning or a loosing position, we are going to put end_of_the_game as false
        if minmax.end_state(board):
            print("The game ended as a draw!") #If we reach to end of the game  - full of pieces, we get a draw!
            print(Time_list)
            return (True,how_many_turns)
        how_many_turns += 1
        if turn == 1:
            moves = [0,1,2,3,4,5,6]
            move = random.choice(moves)
            if Board.is_valid(board,move) == False:
                continue
            start = time.time()
            move2 = minmax.minimax(board, 3, -math.inf, math.inf, True,move) #Get the best move using MINIMAX algorithm!
            end = time.time()
           # print(move2) #- we can check the moves if we have bug....
            Time_list.append([(how_many_turns/2),(move2),(end-start)])
            move = move2[0]
            row = Board.get_next_open_row(board,move)
            Board.move(board,row,move,1)
            if Winning_move.win(board, 1):
                Board.print_board(board)
                print("Player 2 wins!")
                end_of_the_game = False
                print(Time_list)
                return (True,how_many_turns) #we want our test to get a true answer!
                
            Board.print_board(board)
            

         
                
            turn += 1
            turn = turn % 2
            

        else: #The A.I (sort of)
            moves = [0,1,2,3,4,5,6]
            move = random.choice(moves)
            if Board.is_valid(board,move) == False:
                continue
            start = time.time()
            move2 = minmax.minimax(board, 7, -math.inf, math.inf, True,move) #Get the best move using MINIMAX algorithm!
            end = time.time()
           # print(move2) #- we can check the moves if we have bug....
            Time_list.append([(how_many_turns/2),(move2),(end-start)])
            move = move2[0]
            row = Board.get_next_open_row(board,move)
            Board.move(board,row,move,2)
            if Winning_move.win(board, 2):
                Board.print_board(board)
                print("Player 2 wins!")
                end_of_the_game = False
                print(Time_list)
                return (True,how_many_turns) #we want our test to get a true answer!
                
            Board.print_board(board)
            

         
                
            turn += 1
            turn = turn % 2

if __name__ == '__main__':
    board = Board.board()
    main(board)
    

        