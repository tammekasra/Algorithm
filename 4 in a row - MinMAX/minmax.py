

import math
import Board
import random
import numpy as np
import Winning_move
import copy
import main_testing
import Evaluate
x_axis = Board.x_axis
y_axis = Board.y_axis


thisdict = {} 


'''Players next move is a simple algorithm that just blocks opponents winning chances, but does not try to win '''
def players_next_move(board): 
    value = -10 
    print(y_axis)
  
    for i in range(y_axis):
        m = board.copy()
        if i in thisdict:
            if thisdict[i] < 7:
                row = Board.get_next_open_row(m,i)
                Board.move(m,row,i,1)
                if Winning_move.win(m, 1):
                    value = i
                    break
        else:
            continue
    return value

            
''' This check if the board if full or not and if anyone is winning or not'''
def is_end_state(board): #Checks if it is end of the turn!
        if Winning_move.win(board,1):
            return True
        if Winning_move.win(board,2):
            return True
        for i in board:
            for j in i:
                if int(j) == 0:
                    return False                
        return True

''' This just check if the board is full or not '''
def end_state(board): #Checks if it is end of the turn!
        for i in board:
            for j in i:
                if int(j) == 0:
                    return False                
        return True

''' This return if either win, loss or a draw in a given position  '''
def value(board): #We want to get a value to a board, whether its winning for 1 or 2.
        if Winning_move.win(board,2):
            return 1
        if Winning_move.win(board,1):
            return -1

        return 0

''' This checks if the row 7 is full or not, meaning we cannot put more coins there if it is full '''
def get_valid_locations(board):
    locations = []

    for i in range(7):
        if Board.is_valid(board,i):
            locations.append(i)
    random.shuffle(locations)
    return locations

def minimax(board, depth, alpha, beta, A_I,move):
    valid_locations = get_valid_locations(board)
    ''' This checks if a given depth is reached '''
    if depth == 0:
        if A_I: 
            return (move, (Evaluate.score(board, 2)))
        else:
            return (move, -1*(Evaluate.score(board, 1)))
    is_terminal = is_end_state(board)
    if is_terminal:
        if Winning_move.win(board,2):
            return (move,math.inf)
        elif Winning_move.win(board,1):
            return (move,-math.inf)
        else:
            return (move,0)
        
    if A_I: # The artificial intelligence turn (its best move)
        value = -math.inf #(we try to find the maximum value or the result)
        column = 0
        for col in valid_locations:
            row = Board.get_next_open_row(board,col)
            b_copy = board.copy()  # We need to copy the board, otherwise it going to be mixed up within the recursion file
            Board.move(b_copy,row,col,2)
            new_score = minimax(b_copy, depth-1, alpha, beta, False,col)[1]
            if new_score > value:
                value = new_score
                column = col
            alpha = max(alpha, value)
            if alpha >= beta:
                break
        return (column, value)

    else: # Our as the players maximimum turn
        value = math.inf
        column = 0
        for col in valid_locations:
            row = Board.get_next_open_row(board,col)
            b_copy = board.copy()
            Board.move(b_copy,row,col,1)
            new_score = minimax(b_copy, depth-1, alpha, beta, True,col)[1]
            if new_score < value:
                value = new_score
                column = col
            beta = min(beta, value)
            if alpha >= beta:
                break
        return (column, value)





