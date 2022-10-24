

import random
import sys
import math
import numpy as np
import pygame

import Board
import draw_board
import minmax
import Winning_move












another_algorithm_tofight_against_AI = int(input("Please select player(1) or a bot against the A.I (2)  "))

''' Whos turns is it - player 1 is always 1 and 2 in this case is 0 '''
turn = 0
'''All GUI starts with init() '''


'''We get the empty board from board module '''
board = Board.board()
Board.print_board(board)

'''If the game ends, it turns True and the while loop will stop '''
game_over = False

pygame.init()


'''The size of the box '''
size = (700, 700)

'''Initiate the screen '''
screen = pygame.display.set_mode(size)

'''We are drawings the board - GUI '''
draw_board.draw(board)

'''We need to update out init() whenever we make a move '''
pygame.display.update()

'''This is just the fond ot he screen '''
myfont = pygame.font.SysFont("FreeMono", 75)
while not game_over:
    if minmax.end_state(board):
            print("The game ended as a draw!") #If we reach to end of the game  - full of pieces, we get a draw!
            label = myfont.render("The game ended as a draw!", 1, (255, 255, 0))
            screen.blit(label, (40, 10))
            game_over = True
            
           
       
    if another_algorithm_tofight_against_AI == 1: 
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.MOUSEMOTION:
                pygame.draw.rect(screen, (0, 0, 0), (0, 0, 700, 100))
                posx = event.pos[0]
                if turn == 0:
                    pygame.draw.circle(screen, (255, 0, 0), (posx, int(50)), 45)
            pygame.display.update()
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                    # #Ask player 1 for input
                    if turn == 0:
                        posx = event.pos[0]
                        col = int(math.floor(posx/100))

                        if Board.is_valid(board, col):
                            row = Board.get_next_open_row(board, col)
                            Board.move(board, row, col, 1)

                            if Winning_move.win(board, 1):
                                pygame.draw.rect(screen, (0, 0, 0), (0, 0, 700, 100))
                                label = myfont.render("Player 1 is victorious!", 1, (255, 0, 0))
                                screen.blit(label, (40, 10))
                                game_over = True

                            turn += 1
                            turn = turn % 2

                            draw_board.draw(board)
    if another_algorithm_tofight_against_AI ==  2:
        moves = [0,1,2,3,4,5,6]
        move = random.choice(moves)
        if Board.is_valid(board,move) == False:
                continue
      
        move2 = minmax.minimax(board, 5, -math.inf, math.inf, True,move) #Get the best move using MINIMAX algorithm!
        col = move2[0]
        if Board.is_valid(board, col):
            row = Board.get_next_open_row(board, col)
            Board.move(board, row, col, 1)

            pygame.time.wait(5000)

            if Winning_move.win(board, 1):
                pygame.draw.rect(screen, (0, 0, 0), (0, 0, 700, 100))
                label = myfont.render("Player 1 is victorious!", 1, (255, 0, 0))
                screen.blit(label, (40, 10))
                game_over = True

            Board.print_board(board)
            draw_board.draw(board)

            turn += 1
            turn = turn % 2


    if turn == 1 and not game_over:
        moves = [0,1,2,3,4,5,6]
        move = random.choice(moves)
        if Board.is_valid(board,move) == False:
                continue
      
        move2 = minmax.minimax(board, 5, -math.inf, math.inf, True,move) #Get the best move using MINIMAX algorithm!
        col = move2[0]
        if Board.is_valid(board, col):
            row = Board.get_next_open_row(board, col)
            Board.move(board, row, col, 2)

            pygame.time.wait(5000)

            if Winning_move.win(board, 2):
                pygame.draw.rect(screen, (0, 0, 0), (0, 0, 700, 100))
                label = myfont.render("Player 2 is victorious!", 1, (255, 255, 0))
                screen.blit(label, (40, 10))
                game_over = True

            Board.print_board(board)
            draw_board.draw(board)

            turn += 1
            turn = turn % 2

    if(game_over):
        pygame.time.wait(2000)


