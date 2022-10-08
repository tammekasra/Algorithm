



import numpy as np
import Board
import Winning_move
import random
import minmax
import pygame
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
    another_algorithm_tofight_against_AI = int(input("Please select player(1) or a bot against the A.I (2)  "))
    while end_of_the_game: #If we reach to either a winning or a loosing position, we are going to put end_of_the_game as false
        if minmax.end_state(board):
            print("The game ended as a draw!") #If we reach to end of the game  - full of pieces, we get a draw!
            print(Time_list)
            return (True,how_many_turns)
        how_many_turns += 1
        if turn == 0:
            if another_algorithm_tofight_against_AI == 1:
                move = int(input("Player 1, Make your Selection(0-6):  "))

                if move < 0 or move > 6: #If we select a wrong slot
                    print("Please select a proper slot!")
                    continue

              #  if move in minmax.thisdict:  #This will check if the slot is full or not (max is 7)
              #      if minmax.thisdict[move] == 6:
              #          print("Please select another slot since this is FULL!")
              #          continue
              #  if move not in minmax.thisdict: #We will use a dict, since it is a lot easier and faster to do this way
              #      minmax.thisdict[move] = 1
              #  else:
              #      minmax.thisdict[move] = minmax.thisdict[move] + 1


                
                if Board.is_valid(board,move): #Is_valid move checks if the move can be played or not (if is it over the select column or not which is 6)
                    row = Board.get_next_open_row(board,move) #We will fetch the desired row where we can to insert our coin - since the number of the row will change everytime
                    Board.move(board,row,move,1) #We insert the wanted move
            #      Board.print_board(board)
                    if Winning_move.win(board, 1): #We check if it is a winning game!
                                print("Player 1 wins!")
                                end_of_the_game = False 
                                print(Time_list)
                                return (False,how_many_turns)   # We return false if and only if the player 1 wins (A.I has to either win or get a draw), we need to modify something if the test comes out as negative!
                                break
                else:
                    
                    continue
                
                Board.print_board(board) # We need to print it the matrix upside down
                turn += 1
                turn = turn % 2
            else:
                moves = [0,1,2,3,4,5,6]
                move2 = random.choice(moves)
                if Board.is_valid(board,move2) == False:
                    continue
                move = minmax.minimax(board, 5, -math.inf, math.inf, True,move2)[0]
                if move < 0 or move > 6: #If we select a wrong slot
                    print("The slot is full")
                    continue

               # if move in minmax.thisdict:  #This will check if the slot is full or not (max is 7)
               #     if minmax.thisdict[move] == 6:
               #         print("Please select another slot since this is FULL!")
               #         continue
               # if move not in minmax.thisdict: #We will use a dict, since it is a lot easier and faster to do this way
               #     minmax.thisdict[move] = 1
               # else:
               #     minmax.thisdict[move] = minmax.thisdict[move] + 1


                
                if Board.is_valid(board,move): #Is_valid move checks if the move can be played or not (if is it over the select column or not which is 6)
                    row = Board.get_next_open_row(board,move) #We will fetch the desired row where we can to insert our coin - since the number of the row will change everytime
                    Board.move(board,row,move,1) #We insert the wanted move
            #      Board.print_board(board)
                    if Winning_move.win(board, 1): #We check if it is a winning game!
                                Board.print_board(board) # We need to print it the matrix upside down
                                print("Player 1 wins!")
                                end_of_the_game = False
                                minmax.thisdict.clear()
                                return (False,how_many_turns)   # We return false if and only if the player 1 wins (A.I has to either win or get a draw), we need to modify something if the test comes out as negative!
                                break
                
                
                turn += 1
                turn = turn % 2

            

        else: #The A.I (sort of)
            moves = [0,1,2,3,4,5,6]
            move = random.choice(moves)
            if Board.is_valid(board,move) == False:
                continue
            start = time.time()
            move2 = minmax.minimax(board, 5, -math.inf, math.inf, True,move) #Get the best move using MINIMAX algorithm!
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
 
