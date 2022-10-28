







import Board
import random
import minmax
import math
import time
x_axis = Board.x_axis # determine the length of the rows
y_axis  = Board.y_axis # determine the length of the columns
 





def main(board):     
    how_many_turns = 0
    Board.print_board(board)
    end_of_the_game = True
    turn = 0
    depth_stronger_ai = 7
    depth_weaker_ai = 3
    Time_list_weak_Ai = 0
    Time_list_strong_Ai = 0
    while end_of_the_game: #If we reach to either a winning or a loosing position, we are going to put end_of_the_game as false
        if minmax.end_state(board):
            print("The game ended as a draw!") #If we reach to end of the game  - full of pieces, we get a draw!
            return (False,Time_list_weak_Ai,Time_list_strong_Ai)
        how_many_turns += 1
        if turn == 0:
            moves = [0,1,2,3,4,5,6]
            move = random.choice(moves)
            if Board.is_valid(board,move) == False:
                continue
            start = time.time()
            move2 = minmax.minimax(board, depth_weaker_ai, -math.inf, math.inf, True,move) #Get the best move using MINIMAX algorithm!
            end = time.time()
            Time_list_weak_Ai += end - start
           # print(move2) #- we can check the moves if we have bug....
            move = move2[0]
            row = Board.get_next_open_row(board,move)
            Board.move(board,row,move,1)
            if minmax.win(board, 1):
                Board.print_board(board)
                print("Player 2 wins!")
                end_of_the_game = False
                print(Time_list_weak_Ai,Time_list_strong_Ai)
                return (False,Time_list_weak_Ai,Time_list_strong_Ai) #we want our test to get a true answer!
                
            Board.print_board(board)
            

         
                
            turn += 1
            turn = turn % 2
            

        else: #The A.I (sort of)
            moves = [0,1,2,3,4,5,6]
            move = random.choice(moves)
            if Board.is_valid(board,move) == False:
                continue
            start2 = time.time()
            move2 = minmax.minimax(board, depth_stronger_ai, -math.inf, math.inf, True,move) #Get the best move using MINIMAX algorithm!
            end2 = time.time()
           # print(move2) #- we can check the moves if we have bug....
            Time_list_strong_Ai +=  end2-start2
            move = move2[0]
            eval = move2[1]
            row = Board.get_next_open_row(board,move)
            Board.move(board,row,move,2)
            if math.isinf(eval):
                if minmax.win(board, 2):
                    Board.print_board(board)
                    print("Player 2 wins!")
                    end_of_the_game = False
                    print(Time_list_weak_Ai,Time_list_strong_Ai)
                    return (True,Time_list_weak_Ai,Time_list_strong_Ai) #we want our test to get a true answer!
                
            Board.print_board(board)
            

         
                
            turn += 1
            turn = turn % 2

if __name__ == '__main__':
    board = Board.board()
    main(board)
    

        