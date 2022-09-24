


import Board
import numpy as np
import Winning_move
import copy
x_axis = Board.x_axis
y_axis = Board.y_axis


thisdict = {}


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


def Generate_Children(board,turn):

    list = []

    for move in range(7):
            board2 = board.copy()
            row = Board.get_next_open_row(board2,move)
            Board.move(board2,row,move,turn)
            list.append(board2)
            
    return list
            

def minimax(board):
    
    for children in Generate_Children(board,2):
        Board.print_board(children)






