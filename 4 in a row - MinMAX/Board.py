import numpy as np

 
x_axis = 6
y_axis = 7
 

def board():
    board = np.zeros((6,7))
    return board
 
def move(board,row,col,piece):
    board[row][col]= piece
 
def is_valid(board,col):
    return board[5][col]==0
 
def get_next_open_row(board,col):
    for r in range(x_axis):
        if board[r][col]==0:
            return r
     
def print_board(board):
    print(np.flip(board,0))