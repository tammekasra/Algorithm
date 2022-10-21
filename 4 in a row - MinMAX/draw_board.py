import math 
import pygame

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