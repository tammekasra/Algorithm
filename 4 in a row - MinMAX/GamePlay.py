

import random
import math
import pygame
import Board
import minmax
import sys







a_i_or_player = 1













def play():
    ''' Whos turns is it - player 1 is always 1 and 2 in this case is 0 '''
    turn = random.choice([1,0])
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
    Board.draw(board)

    '''We need to update out init() whenever we make a move '''
    pygame.display.update()

    '''This is just the fond ot he screen '''
    myfont = pygame.font.SysFont("FreeMono", 75)

    while not game_over:

        if minmax.end_state(board):
                label = myfont.render("Draw!", 1, (255, 255, 0))
                screen.blit(label, (40, 10))
                game_over = True
                
            
        
        if a_i_or_player == 1:
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

                                    if minmax.win(board, 1):
                                        pygame.draw.rect(screen, (0, 0, 0), (0, 0, 700, 100))
                                        abel = myfont.render("You won!", 1, (255, 255, 0))
                                        screen.blit(label, (40, 10))
                                        game_over = True

                                    turn += 1
                                    turn = turn % 2

                                    Board.draw(board)
        else:
            if turn == 0 and not game_over:
                    moves = [0,1,2,3,4,5,6]
                    while True:
                        move = random.choice(moves)
                        if Board.is_valid(board,move) == True:
                            break
                    
                
                    move2 = minmax.minimax(board, 6, -math.inf, math.inf, True,move) #Get the best move using MINIMAX algorithm!
                    col = move2[0]
                    eval = move2[1]
                    if Board.is_valid(board, col):
                        row = Board.get_next_open_row(board, col)
                        Board.move(board, row, col, 1)
                        if math.isinf(eval):
                            if minmax.win(board, 1):
                                pygame.draw.rect(screen, (0, 0, 0), (0, 0, 700, 100))
                                label = myfont.render("A.I wins!", 1, (255, 255, 0))
                                screen.blit(label, (40, 10))
                                game_over = True

                        Board.print_board(board)
                        Board.draw(board)

                        turn += 1
                        turn = turn % 2
            

        if turn == 1 and not game_over:
                moves = [0,1,2,3,4,5,6]
                while True:
                    move = random.choice(moves)
                    if Board.is_valid(board,move) == True:
                        break
                
            
                move2 = minmax.minimax(board, 5, -math.inf, math.inf, True,move) #Get the best move using MINIMAX algorithm!
                col = move2[0]
                eval = move2[1]
                print(eval)
                if Board.is_valid(board, col):
                    row = Board.get_next_open_row(board, col)
                    Board.move(board, row, col, 2)
                    if minmax.win(board, 2):
                        pygame.draw.rect(screen, (0, 0, 0), (0, 0, 700, 100))
                        label = myfont.render("A.I wins!", 1, (255, 255, 0))
                        screen.blit(label, (40, 10))
                        game_over = True

                    Board.print_board(board)
                    Board.draw(board)

                    turn += 1
                    turn = turn % 2

        if(game_over):
                pygame.time.wait(5000)


