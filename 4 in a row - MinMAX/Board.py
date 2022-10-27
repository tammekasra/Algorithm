import numpy as np
import pygame
 
x_axis = 6
y_axis = 7
 


def board(): #here we make the size of the board which is 6 columns and 7 rows
    board = np.zeros((6,7)) 
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



''' This is just the pygame drawing... still have no clue how it fully works... '''
BLUE = (255, 127, 14)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
YELLOW = (31, 119, 180)
SQUARESIZE = 100

width = 700
height = 700
RADIUS = 45
size = (700, 700)

screen = pygame.display.set_mode(size)

def draw(board):
    for q in range(7):
        for p in range(6):
            pygame.draw.rect(screen, BLUE, (q * SQUARESIZE, p * SQUARESIZE + SQUARESIZE, SQUARESIZE, SQUARESIZE))
            pygame.draw.circle(screen, BLACK, (
            int(q * SQUARESIZE + SQUARESIZE / 2), int(p * SQUARESIZE + SQUARESIZE + SQUARESIZE / 2)), RADIUS)

    for c in range(7):
        for r in range(6):
            if board[r][c] ==1:
                pygame.draw.circle(screen, RED, (
                int(c * SQUARESIZE + SQUARESIZE / 2), height - int(r * SQUARESIZE + SQUARESIZE / 2)), RADIUS)
            elif board[r][c] == 2:
                pygame.draw.circle(screen, YELLOW, (
                int(c * SQUARESIZE + SQUARESIZE / 2), height - int(r * SQUARESIZE + SQUARESIZE / 2)), RADIUS)
    pygame.display.update()