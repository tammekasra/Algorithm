import numpy as np

 
x_axis = 6
y_axis = 7
 

def board(): #here we make the size of the board which is 6 columns and 7 rows
    board = np.zeros((6,7)) 
    return board

def reset(board):
    for i in board:
        for j in i:
            j = 0
    return board
 
def move(board,row,col,piece): #we put our desired move in the column we want
    board[row][col]= piece
 
def is_valid(board,col): #we check if it is valid or not that we can put it in the the column (it might be full)
    return board[5][col]==0
 
def get_next_open_row(board,col): #Here when we determine in which ROW we are inserting our results (since it is increasing everytime)
    for r in range(x_axis):
        if board[r][col]==0:
            return r
     
def print_board(board): #since numpy prints from top left to bottom left, we flip the board so we can be seen. 
    print(np.flip(board,0))