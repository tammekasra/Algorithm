import numpy as np



''' Number of row and columns'''
x_axis = 6
y_axis = 7
 



 
'''This puts the piece in the column and therefor cannot be putten there again '''
def move(board,row,col,piece): 
    board[row][col]= piece

'''We have to check whether the move that we want to play is vali -e.g if the column isnt full, so the maximum row is 5  ''' 
def is_valid(board,col): 
    return board[5][col]==0

''' We get the next row after we have played in a given slot  ''' 
def get_next_open_row(board,col): 
    for r in range(x_axis):
        if board[r][col]==0:
            return r

'''Since numpy arrays starts from left up, but the game is from down to up, so we need to flip it (within the program it is never flipepd) '''     
def print_board(board): 
    print(np.flip(board,0))



