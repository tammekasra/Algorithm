



import numpy as np
import Board
import Winning_move
import random
import minmax
import pygame
import sys
import math
import time
x_axis = Board.x_axis # determine the length of the rows
y_axis  = Board.y_axis # determine the length of the columns
 


BLUE = (0,0,255)
BLACK = (0,0,0)
RED = (255,0,0)
YELLOW = (255,255,0)
 
ROW_COUNT = 6
COLUMN_COUNT = 7

import numpy as np
import pygame
import sys
import math
 
BLUE = (0,0,255)
BLACK = (0,0,0)
RED = (255,0,0)
YELLOW = (255,255,0)
 
ROW_COUNT = 6
COLUMN_COUNT = 7
 
def create_board():
    board = np.zeros((ROW_COUNT,COLUMN_COUNT))
    return board
 
def drop_piece(board, row, col, piece):
    board[row][col] = piece
 
def is_valid_location(board, col):
    return board[ROW_COUNT-1][col] == 0
 
def get_next_open_row(board, col):
    for r in range(ROW_COUNT):
        if board[r][col] == 0:
            return r
 
def print_board(board):
    print(np.flip(board, 0))
 
def winning_move(board, piece):
    # Check horizontal locations for win
    for c in range(COLUMN_COUNT-3):
        for r in range(ROW_COUNT):
            if board[r][c] == piece and board[r][c+1] == piece and board[r][c+2] == piece and board[r][c+3] == piece:
                return True
 
    # Check vertical locations for win
    for c in range(COLUMN_COUNT):
        for r in range(ROW_COUNT-3):
            if board[r][c] == piece and board[r+1][c] == piece and board[r+2][c] == piece and board[r+3][c] == piece:
                return True
 
    # Check positively sloped diaganols
    for c in range(COLUMN_COUNT-3):
        for r in range(ROW_COUNT-3):
            if board[r][c] == piece and board[r+1][c+1] == piece and board[r+2][c+2] == piece and board[r+3][c+3] == piece:
                return True
 
    # Check negatively sloped diaganols
    for c in range(COLUMN_COUNT-3):
        for r in range(3, ROW_COUNT):
            if board[r][c] == piece and board[r-1][c+1] == piece and board[r-2][c+2] == piece and board[r-3][c+3] == piece:
                return True
 
def draw_board(board):
    for c in range(COLUMN_COUNT):
        for r in range(ROW_COUNT):
            pygame.draw.rect(screen, BLUE, (c*SQUARESIZE, r*SQUARESIZE+SQUARESIZE, SQUARESIZE, SQUARESIZE))
            pygame.draw.circle(screen, BLACK, (int(c*SQUARESIZE+SQUARESIZE/2), int(r*SQUARESIZE+SQUARESIZE+SQUARESIZE/2)), RADIUS)
     
    for c in range(COLUMN_COUNT):
        for r in range(ROW_COUNT):      
            if board[r][c] == 1:
                pygame.draw.circle(screen, RED, (int(c*SQUARESIZE+SQUARESIZE/2), height-int(r*SQUARESIZE+SQUARESIZE/2)), RADIUS)
            elif board[r][c] == 2: 
                pygame.draw.circle(screen, YELLOW, (int(c*SQUARESIZE+SQUARESIZE/2), height-int(r*SQUARESIZE+SQUARESIZE/2)), RADIUS)
    pygame.display.update()
 
 

game_over = False
turn = 0
 
#initalize pygame
pygame.init()
 
#define our screen size
SQUARESIZE = 100
 
#define width and height of board
width = COLUMN_COUNT * SQUARESIZE
height = (ROW_COUNT+1) * SQUARESIZE
 
size = (width, height)
 
RADIUS = int(SQUARESIZE/2 - 5)
 
screen = pygame.display.set_mode(size)
#Calling function draw_board again

 
myfont = pygame.font.SysFont("monospace", 75)

def draw_board(board):
    for c in range(COLUMN_COUNT):
        for r in range(ROW_COUNT):
            pygame.draw.rect(screen, BLUE, (c*SQUARESIZE, r*SQUARESIZE+SQUARESIZE, SQUARESIZE, SQUARESIZE))
            pygame.draw.circle(screen, BLACK, (int(c*SQUARESIZE+SQUARESIZE/2), int(r*SQUARESIZE+SQUARESIZE+SQUARESIZE/2)), RADIUS)
     
    for c in range(COLUMN_COUNT):
        for r in range(ROW_COUNT):      
            if board[r][c] == 1:
                pygame.draw.circle(screen, RED, (int(c*SQUARESIZE+SQUARESIZE/2), height-int(r*SQUARESIZE+SQUARESIZE/2)), RADIUS)
            elif board[r][c] == 2: 
                pygame.draw.circle(screen, YELLOW, (int(c*SQUARESIZE+SQUARESIZE/2), height-int(r*SQUARESIZE+SQUARESIZE/2)), RADIUS)
    pygame.display.update()


def main(board):     
    how_many_turns = 0
    draw_board(board)
    pygame.display.update()
    Board.print_board(board)
    end_of_the_game = True
    turn = 0
    Time_list = []
    another_algorithm_tofight_against_AI = int(input("Please select player(1) or a bot against the A.I (2)  "))
    while end_of_the_game: #If we reach to either a winning or a loosing position, we are going to put end_of_the_game as false
        if minmax.end_state(board):
            print("The game ended as a draw!") #If we reach to end of the game  - full of pieces, we get a draw!
            print(Time_list)
            return (True,how_many_turns)
        how_many_turns += 1
        if turn == 0:
            if another_algorithm_tofight_against_AI == 1:
                move = int(input("Player 1, Make your Selection(0-6):  "))

                if move < 0 or move > 6: #If we select a wrong slot
                    print("Please select a proper slot!")
                    continue

                
                if Board.is_valid(board,move): #Is_valid move checks if the move can be played or not (if is it over the select column or not which is 6)
                    row = Board.get_next_open_row(board,move) #We will fetch the desired row where we can to insert our coin - since the number of the row will change everytime
                    Board.move(board,row,move,1) #We insert the wanted move
            #      Board.print_board(board)
                    if Winning_move.win(board, 1): #We check if it is a winning game!
                                print("Player 1 wins!")
                                end_of_the_game = False 
                                print(Time_list)
                                return (False,how_many_turns)   # We return false if and only if the player 1 wins (A.I has to either win or get a draw), we need to modify something if the test comes out as negative!
                                break
            else:
                    
                    moves = [0,1,2,3,4,5,6]
                    move = random.choice(moves)
                    if Board.is_valid(board,move) == False:
                        continue
                    start = time.time()
                    move2 = minmax.minimax(board, 5, -math.inf, math.inf, True,move) #Get the best move using MINIMAX algorithm!
                    end = time.time()
                # print(move2) #- we can check the moves if we have bug....
                    Time_list.append([(how_many_turns/2),(move2),(end-start)])
                    move = move2[0]
                    row = Board.get_next_open_row(board,move)
                    Board.move(board,row,move,1)
                    if Winning_move.win(board, 1):
                        Board.print_board(board)
                        print("Player 2 wins!")
                        end_of_the_game = False
                        print(Time_list)
                        return (True,how_many_turns) #we want our test to get a true answer!
                
            Board.print_board(board) # We need to print it the matrix upside down
            turn += 1
            turn = turn % 2
          
                

            

        else: #The A.I (sort of)
            moves = [0,1,2,3,4,5,6]
            move = random.choice(moves)
            if Board.is_valid(board,move) == False:
                continue
            start = time.time()
            move2 = minmax.minimax(board, 5, -math.inf, math.inf, True,move) #Get the best move using MINIMAX algorithm!
            end = time.time()
           # print(move2) #- we can check the moves if we have bug....
            Time_list.append([(how_many_turns/2),(move2),(end-start)])
            move = move2[0]
            row = Board.get_next_open_row(board,move)
            Board.move(board,row,move,2)
            if Winning_move.win(board, 2):
                Board.print_board(board)
                print("Player 2 wins!")
                end_of_the_game = False
                print(Time_list)
                return (True,how_many_turns) #we want our test to get a true answer!
                
            Board.print_board(board)
            

         
                
            turn += 1
            turn = turn % 2

if __name__ == '__main__':
    board = Board.board()
    main(board)
    