

import random
import sys
import math
import numpy as np
import pygame

import Board
import draw_board
import minmax
import Winning_move





board = Board.board()
Board.print_board(board)
game_over = False






pygame.init()


size = (700, 700)

screen = pygame.display.set_mode(size)
draw_board.draw(board)
pygame.display.update()

myfont = pygame.font.SysFont("monospace", 75)

turn = 0

while not game_over:
    if minmax.end_state(board):
            print("The game ended as a draw!") #If we reach to end of the game  - full of pieces, we get a draw!
            label = myfont.render("The game ended as a draw!", 1, (255, 255, 0))
            screen.blit(label, (40, 10))
            game_over = True
            
           
       
            
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

            pygame.time.wait(500)

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


