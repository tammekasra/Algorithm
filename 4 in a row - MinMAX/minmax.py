

import math
import Board
import random
import Evaluate
x_axis = Board.x_axis
y_axis = Board.y_axis






""" x axis is the number of rows which is 6 and y axis is the numer of colum which is 7  """
x_axis = Board.x_axis
y_axis  = Board.y_axis

def win(board, piece):
    '''Horizontal checking'''
    
    for y in range(y_axis-3):
        for x in range(x_axis):
            if   board[x][y] == piece and board[x][y+1] == piece and board[x][y+2] == piece and board[x][y+3] == piece:
                return True
 
    '''Vertical checking'''
    for y in range(y_axis):
        for x in range(x_axis-3):
            if  board[x][y] == piece and board[x+1][y] == piece and board[x+2][y] == piece and board[x+3][y] == piece:
                return True
 
    '''Diagonal checking'''
    for y in range(y_axis-3):
        for x in range(x_axis-3):
            if  board[x][y] == piece and board[x+1][y+1] == piece and board[x+2][y+2] == piece and board[x+3][y+3] == piece:
                return True
 
    '''Diagonal checking'''
    for y in range(y_axis-3):
        for x in range(3, x_axis):
            if  board[x][y] == piece and board[x-1][y+1] == piece and board[x-2][y+2] == piece and board[x-3][y+3] == piece:
                return True




            
''' This check if the board if full or not and if anyone is winning or not'''
def is_end_state(board): 
        if win(board,1):
            return True
        if win(board,2):
            return True
        for i in board:
            for j in i:
                if int(j) == 0:
                    return False                
        return True

''' This just check if the board is full or not '''
def end_state(board): 
        for i in board:
            for j in i:
                if int(j) == 0:
                    return False                
        return True


''' This checks if the row 7 is full or not, meaning we cannot put more coins there if it is full '''
def get_valid_locations(board):
    locations = []
    for i in range(7):
        if Board.is_valid(board,i):
           locations.append(i)
           
    ''' We want to shuffle all the time just go check whether the testing is proper or not (might go through all the possible positions)'''
    random.shuffle(locations)

    return locations 




def minimax(board, depth, alpha, beta, A_I,move):
    valid_locations = get_valid_locations(board)
    ''' This checks if a given depth is reached '''
    if depth == 0:
            ''' This gives gives the overall evaluation using alpha-pruning or in this case evaluation, and we change the value always by -1   '''
            return (move, -1*(Evaluate.score(board, 1)))
    is_terminal = is_end_state(board)
    if is_terminal:
        if win(board,2):
            return (move,math.inf)
        elif win(board,1):
            return (move,-math.inf)
        else:
            return (move,0)

    '''The artificial intelligence turn (its best move) '''
    if A_I: 
        value = -math.inf 
        column = 0
        for col in valid_locations:
            row = Board.get_next_open_row(board,col)
            b_copy = board.copy()  # We need to copy the board, otherwise it going to be mixed up within the recursion file
            Board.move(b_copy,row,col,2)
            new_score = minimax(b_copy, depth-1, alpha, beta, False,col)[1]
            if new_score > value:
                value = new_score
                column = col
            if alpha >= beta:
                break
            alpha = max(alpha, value)
        return (column, value)


        '''THis is our turn '''
    else: 
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
            if alpha >= beta:
                break
            beta = min(beta, value)
        return (column, value)





