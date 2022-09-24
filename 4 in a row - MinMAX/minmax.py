


import Board
import numpy as np
import Winning_move
import copy
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


def Generate_Children(board,turn): #When we go through minimax algorithm, the core essence is to go through all possible combinations!

    list = []

    for move in range(7):
        if Board.is_valid(board,move):
            board2 = board.copy()
            row = Board.get_next_open_row(board2,move)
            Board.move(board2,row,move,turn)
            list.append(board2)
        else:
            continue
            
    return list
            

def is_end_state(board): #Checks if it is end of the turn!
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

def minimax(board): #The main starting to point for min-max pruning (back a forth!)

    move = 0
    for i in range(6): #It goes trhough 7 columns (0-6) and tries all possible options
        if Board.is_valid(board,i): #
            a = max_value(board,0,0,0,i) #if get the optimal MOVE, we insert the current board, then alpha value, to find the
                                          #the biggest value if there is one (1), and beta which is minimum value -1, level is the 
                                          #  for how long we want to predict our optimal move, and i is the current move, if it is bad or not 
            if a[0] == 0 or a[0] == -1:
                move = a[1]
                break

    return move

def max_value(board, alpha, beta,level,move):
    # Implement me
    v = -1
    if level == 5:
        if Winning_move.win(board,2):
            return (v,move)
        else:
            return (0,move)
    if Winning_move.win(board,2):
        return (v,move)
    if is_end_state(board): return (0,move) #return if we won
    for children in Generate_Children(board,2):
        #Board.print_board(children)
        c = min_value(children,alpha,beta,level+1,move)
        v = max(v, int(c[0]))
        alpha = max(alpha, v)
        if alpha >= beta: return (v,move)
    return (v,move)

def min_value(board, alpha, beta,level,move):
    v = 1
    if level == 5:
        if Winning_move.win(board,1):
            return (v,move)
        else:
            return (0,move)
    if is_end_state(board): return (0,move) #Discrd the current board, if it is loosing!
    for children in Generate_Children(board,1):
        #Board.print_board(children)
        c = max_value(children,alpha,beta,level+1,move) #at the end of the root, we find either -1,0,1 and by each step decide if we pick
        v = min(v, int(c[0])) #-1 , 0 or 1 but in this case  
        beta = min(beta, v)
        if alpha >= beta: return (v,move)
    return (v,move)






