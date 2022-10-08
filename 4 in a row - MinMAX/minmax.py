

import math
import Board
import random
import numpy as np
import Winning_move
import copy
import Evaluate
x_axis = Board.x_axis
y_axis = Board.y_axis


thisdict = {} #How many coins we have on each column!


def players_next_move(board): #This is a not the main algorithm (this is an algorithm that stops the user by wining on move 4)
    value = -10 #The main algorith MINIMAX is below, this agorithm is just for fun, and can be used later it to play against the main A.I
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
def end_state(board): #Checks if it is end of the turn!
        for i in board:
            for j in i:
                if int(j) == 0:
                    return False                
        return True


def value(board): #We want to get a value to a board, whether its winning for 1 or 2.
        if Winning_move.win(board,2):
            return 1
        if Winning_move.win(board,1):
            return -1

        return 0

def get_valid_locations(board):
    locations = []

    for i in range(7):
        if Board.is_valid(board,i):
            locations.append(i)
    random.shuffle(locations)
    return locations

def minimax(board, depth, alpha, beta, A_I,move):
    valid_locations = get_valid_locations(board)
    
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

#def minimax(board): #The main starting to point for min-max pruning (back a forth!)

 #   move = max_value(board,-1,1,10000)

 #   return move

#def max_value(board, alpha, beta,level,move):
    # Implement me
#    v = -1
#    if level == 5:
#        return value(board)
#    if Winning_move.win(board,2):
#        return (v,move)
#    if is_end_state(board): return (0,move) #return if we won
#    for children in Generate_Children(board,2):
#        #Board.print_board(children)
#        c = min_value(children,alpha,beta,level+1,move)
#        v = max(v, int(c[0]))
#        if value >= beta: return (v,move)
#        alpha = max(alpha, v)
        
#    return (v,move)

#def min_value(board, alpha, beta,level,move):
#    v = 1
#    if level == 5:
#        return value(board)
#    if is_end_state(board): return (0,move) #Discrd the current board, if it is loosing!
#    for children in Generate_Children(board,1):
#        #Board.print_board(children)
#        c = max_value(children,alpha,beta,level+1,move) #at the end of the root, we find either -1,0,1 and by each step decide if we pick
#        v = min(v, int(c[0])) #-1 , 0 or 1 but in this case  
#        beta = min(beta, v)
#        if alpha >= beta: return (v,move)
#    return (v,move)






