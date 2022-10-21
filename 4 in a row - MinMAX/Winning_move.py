import Board
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