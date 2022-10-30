

import Board
import minmax

x_axis = Board.x_axis # determine the length of the rows
y_axis  = Board.y_axis # determine the length of the columns
'''Players next move is a simple algorithm that just blocks opponents winning chances, but does not try to win '''
def players_next_move(board): 
    value = -10 
  
    for i in range(y_axis):
        m = board.copy()
       
        if Board.is_valid(board,i):
                row = Board.get_next_open_row(m,i)
                Board.move(m,row,i,1)
                if minmax.win(m, 1):
                    value = i
                    break
        else:
            continue
    return value
