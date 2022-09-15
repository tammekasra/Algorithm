


import Board
import numpy as np
import Winning_move
import copy
x_axis = Board.x_axis
y_axis = Board.y_axis


def players_next_move(board):
    value = -10
    print(y_axis)
    for i in range(y_axis):
        m = board.copy()
        row = Board.get_next_open_row(m,i)
        Board.move(m,row,i,1)
        if Winning_move.win(m, 1):
                    value = i
                    break
    return value






